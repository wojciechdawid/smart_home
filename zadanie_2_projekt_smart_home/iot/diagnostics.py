from zadanie_2_projekt_smart_home.iot.device import Device


def collect_diagnostics(device: Device) -> None:
    """Function for collecting diagnostics"""
    print("Connecting to diagnostics server.")
    print(f"Sending status update {device.status_update()} to server.")
