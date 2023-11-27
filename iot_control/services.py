import pickle
import string
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
import random
from .models import Message

from iot_control.models import Message


def generate_id() -> str:
    return ''.join(random.choices(string.ascii_uppercase, k=10))


class MessageType(Enum):
    SWITCH_ON = auto()
    SWITCH_OFF = auto()
    CHANGE_COLOR = auto()
    PLAY_SONG = auto()
    OPEN = auto()
    CLOSE = auto()


@dataclass
class MessageDTO:
    device_id: str
    msg_type: MessageType
    data: str

    @classmethod
    def from_django_model(cls, msg_service: Message) -> 'MessageDTO':
        message_types = {
            "SWITCH_ON": MessageType.SWITCH_ON,
            "SWITCH_OFF": MessageType.SWITCH_OFF,
            "CHANGE_COLOR": MessageType.CHANGE_COLOR,
            "PLAY_SONG": MessageType.PLAY_SONG,
            "OPEN": MessageType.OPEN,
            "CLOSE": MessageType.CLOSE
        }
        return MessageDTO(
            device_id=msg_service.device_id,
            msg_type=message_types[msg_service.msg_type],
            data=msg_service.data
        )


class Device(ABC):
    @abstractmethod
    def connect(self) -> None:
        """Method for connect"""

    @abstractmethod
    def disconnect(self) -> None:
        """Method for disconnect"""

    @abstractmethod
    def send_message(self, message_type: MessageType, data: str) -> str:
        """Method for sending message"""

    @abstractmethod
    def status_update(self) -> str:
        """Method for updating status"""


class HueLight(Device):
    def connect(self) -> str:
        return "Connecting Hue Light"

    def disconnect(self) -> str:
        return "Disonnecting Hue Light"

    def send_message(self, message_type: MessageType, data: str) -> str:
        return f"Hue light handling message of type {message_type.name} with data [{data}]"

    def status_update(self) -> str:
        return "hue_light_status_ok"


class SmartSpeaker(Device):
    def connect(self) -> str:
        return "Connecting Smart Speaker"

    def disconnect(self) -> str:
        return "Disonnecting Smart Speaker"

    def send_message(self, message_type: MessageType, data: str) -> str:
        return f"Smart Speaker handling message of type {message_type.name} with data [{data}]"

    def status_update(self) -> str:
        return "smart_speaker_status_ok"


class Curtains(Device):
    def connect(self) -> str:
        return "Connecting Curtains"

    def disconnect(self) -> str:
        return "Disonnecting Curtains"

    def send_message(self, message_type: MessageType, data: str) -> str:
        return f"Curtains handling message of type {message_type.name} with data [{data}]"

    def status_update(self) -> str:
        return "curtains_status_ok"


def collect_diagnostics(device: Device) -> str:
    """Function for collecting diagnostics"""
    new_line = "\n"
    return f"Connecting to diagnostics server.{new_line}Sending status update {device.status_update()} to server."


class IOTService:
    devices: list = []
    programs: dict[str, list[MessageDTO]] = {}
    baza_program = "programs.dat"
    devices_file = "devices.dat"

    @classmethod
    def _load_devices(cls) -> list[Device]:
        try:
            with open(cls.devices_file, "rb") as f:
                data = pickle.load(f)
        except FileNotFoundError:
            data = []
        return data

    @classmethod
    def _save_devices(cls, devices: list[Device]):
        with open(cls.devices_file, "wb") as f:
            pickle.dump(devices, f)


    @classmethod
    def register_device(cls, device: int) -> None:
        """Method for registering new devices"""
        device.connect()
        cls.devices = cls._load_devices()
        for dev in cls.devices:
            if device.__class__.__name__ == dev.__class__.__name__:
                return None
        device.id = generate_id()
        cls.devices.append(device)
        cls._save_devices(cls.devices)

    @classmethod
    def unregister_device(cls, device_id: string) -> None:
        """Method for unregistering existing devices"""
        for d in cls.devices:
            if d.id == device_id:
                d.disconnect()

    @classmethod
    def get_device(cls, device_id: str) -> None:
        """Method for removing a device from the list"""
        for d in cls.devices:
            if d.id == device_id:
                cls.devices.remove(d)

    @classmethod
    def run_program(cls, prg_type: str) -> list:
        """Method for running program"""
        cls.programs = cls._load_data()
        msg_list = cls.programs[prg_type]
        out_list = []
        for msg in msg_list:
            for dev in cls.devices:
                if msg.device_id == dev.id:
                    out = dev.send_message(message_type=msg.msg_type, data=msg.data)
                    out_list.append(out)
        msg1 = "=====RUNNING PROGRAM====="
        msg2 = "=====END OF PROGRAM====="
        out_list.insert(0, msg1)
        out_list.insert(len(out_list), msg2)
        return out_list



    @classmethod
    def test_devices(cls) -> list[str]:
        """Method for testing devices"""
        print("Start test devices")
        list_devs = []
        for dev in cls.devices:
            list_devs.append(collect_diagnostics(device=dev))
        return list_devs

    @classmethod
    def create_message(cls, id: str, msg: str, data: str, program_id: str) -> None:
        cls.programs = cls._load_data()
        for dev in cls.devices:
            if id == dev.__class__.__name__:
                device_id = dev.id
        message = Message.objects.create(
            device_id=device_id,
            msg_type=msg,
            data=data
        )
        result = MessageDTO.from_django_model(message)
        msg_list = cls.programs[program_id]
        msg_list.append(result)
        cls.programs.update({program_id: msg_list})
        cls._save_data(cls.programs)

    @classmethod
    def list_messages(cls, list_msg: list[MessageDTO]) -> list[MessageDTO]:
        return list_msg

    @classmethod
    def create_empty_program(cls, program_name: str) -> None:
        if not program_name:
            raise ValueError("Bad name")
        cls.programs = cls._load_data()
        cls.programs[program_name] = []
        cls._save_data(cls.programs)

    @classmethod
    def _load_data(cls) -> dict[str, list[MessageDTO]]:
        try:
            with open(cls.baza_program, "rb") as f:
                data = pickle.load(f)
        except FileNotFoundError:
            data = dict()
        return data

    @classmethod
    def _save_data(cls, programs: dict[str, list[MessageDTO]]):
        with open(cls.baza_program, "wb") as f:
            pickle.dump(programs, f)

    @classmethod
    def get_programs(cls):
        return cls._load_data()


# Create instance of IOTService
iot_service = IOTService()

# Create instances of available devices
hue_light = HueLight()
smart_speaker = SmartSpeaker()
curtains = Curtains()

# Register devices
iot_service.register_device(hue_light)
iot_service.register_device(smart_speaker)
iot_service.register_device(curtains)

# Create programs
hue_light_id = iot_service.devices[0].id
smart_speaker_id = iot_service.devices[1].id
curtains_id = iot_service.devices[2].id
