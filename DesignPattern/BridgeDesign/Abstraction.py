

class RemoteControl:
    def __init__(self, device):
        self.device = device

    def toggle_power(self):
        self.device.toggle_power()

    def volume_down(self):
        self.device.volume_dwon()

    def volume_up(self):
        self.device.volume_up()
