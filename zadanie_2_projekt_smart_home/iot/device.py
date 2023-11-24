from abc import ABC, abstractmethod
from zadanie_2_projekt_smart_home.iot.message import MessageType


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
