from Abstraction import RemoteControl

class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        print("Mute Button Pressed")
        super().volume_down()