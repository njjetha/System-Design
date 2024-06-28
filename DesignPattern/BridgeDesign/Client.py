from RedefinedAbstraction import AdvancedRemoteControl
from ConcreteImplementation import TV
if __name__=="__main__":
    tv=TV()
    arm=AdvancedRemoteControl(TV)
    arm.mute()