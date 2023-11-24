import string
import random

from zadanie_2_projekt_smart_home.iot.device import Device
from zadanie_2_projekt_smart_home.iot.message import Message
from zadanie_2_projekt_smart_home.iot.diagnostics import collect_diagnostics


def generate_id() -> str:
    return ''.join(random.choices(string.ascii_uppercase, k=10))


class IOTService:
    devices: list = []

    @classmethod
    def register_device(cls, device: Device) -> None:
        """Method for registering new devices"""
        device.connect()
        device.id = generate_id()
        cls.devices.append(device)

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
    def run_program(cls, msg_list: list[Message]) -> None:
        """Method for running program"""
        print("=====RUNNING PROGRAM=====")
        for msg in msg_list:
            for dev in cls.devices:
                if msg.device_id == dev.id:
                    dev.send_message(message_type=msg.msg_type, data=msg.data)
        print("=====END OF PROGRAM=====")

    @classmethod
    def test_devices(cls) -> None:
        """Method for testing devices"""
        print("Start test devices")
        for dev in cls.devices:
            collect_diagnostics(device=dev)



