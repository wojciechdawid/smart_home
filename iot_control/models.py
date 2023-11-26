from django.db import models
from enum import Enum, auto


# Create your models here.
class Message(models.Model):
    message_types = [
        ("SWITCH_ON", "SWITCH_ON"),
        ("SWITCH_OFF", "SWITCH_OFF"),
        ("CHANGE_COLOR", "CHANGE_COLOR"),
        ("PLAY_SONG", "PLAY_SONG"),
        ("OPEN", "OPEN"),
        ("CLOSE", "CLOSE"),
    ]
    device_id = models.CharField(max_length=20)
    msg_type = models.CharField(max_length=15, choices=message_types)
    data = models.CharField(max_length=50)
