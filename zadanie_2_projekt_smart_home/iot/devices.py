from zadanie_2_projekt_smart_home.iot.device import Device
from zadanie_2_projekt_smart_home.iot.message import MessageType


class HueLight(Device):
    def connect(self) -> None:
        print("Connecting Hue Light")

    def disconnect(self) -> None:
        print("Disonnecting Hue Light")

    def send_message(self, message_type: MessageType, data: str) -> str:
        print(f"Hue light handling message of type {message_type.name} with data [{data}]")

    def status_update(self) -> str:
        return "hue_light_status_ok"

class SmartSpeaker(Device):
    def connect(self) -> None:
        print("Connecting Smart Speaker")

    def disconnect(self) -> None:
        print("Disonnecting Smart Speaker")

    def send_message(self, message_type: MessageType, data: str) -> None:
        print(f"Smart Speaker handling message of type {message_type.name} with data [{data}]")

    def status_update(self) -> str:
        return "smart_speaker_status_ok"

class Curtains(Device):
    def connect(self) -> None:
        print("Connecting Curtains")

    def disconnect(self) -> None:
        print("Disonnecting Curtains")

    def send_message(self, message_type: MessageType, data: str) -> str:
        print(f"Curtains handling message of type {message_type.name} with data [{data}]")

    def status_update(self) -> str:
        return "curtains_status_ok"
