from Adaptee import LegacySMSService
from Adapter import SMSAdapter
from Target import ModernNotificationService
if __name__=='__main__':
    adaptee=LegacySMSService()
    target=ModernNotificationService()
    adapter=SMSAdapter(target)
    adapter.send_notification("HELLO")


