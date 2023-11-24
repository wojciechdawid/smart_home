from zadanie_2_projekt_smart_home.iot.message import Message, MessageType
from zadanie_2_projekt_smart_home.iot.service import IOTService
from zadanie_2_projekt_smart_home.iot.devices import HueLight, SmartSpeaker, Curtains

if __name__ == "__main__":

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

    # Test devices
    iot_service.test_devices()

    # Create programs
    hue_light_id = iot_service.devices[0].id
    smart_speaker_id = iot_service.devices[1].id
    curtains_id = iot_service.devices[2].id

    wake_up = [
        Message(device_id=hue_light_id, msg_type=MessageType.SWITCH_ON, data="Turn the lights on"),
        Message(device_id=smart_speaker_id, msg_type=MessageType.SWITCH_ON, data="Turn the speakers on"),
        Message(device_id=smart_speaker_id, msg_type=MessageType.PLAY_SONG, data="Play the song"),
        Message(device_id=curtains_id, msg_type=MessageType.OPEN, data="Open curtains"),
    ]

    sleep = [
        Message(device_id=hue_light_id, msg_type=MessageType.SWITCH_OFF, data="Turn the lights off"),
        Message(device_id=smart_speaker_id, msg_type=MessageType.SWITCH_OFF, data="Turn the speakers off"),
        Message(device_id=curtains_id, msg_type=MessageType.CLOSE, data="Close curtains"),
    ]

    # Run programs
    iot_service.run_program(msg_list=wake_up)
    iot_service.run_program(msg_list=sleep)

    # Unregister devices
    for dev in iot_service.devices:
        iot_service.unregister_device(dev)

    # Remove devices
    for dev in iot_service.devices:
        iot_service.get_device(dev)
