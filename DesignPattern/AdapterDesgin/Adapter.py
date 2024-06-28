from Adaptee import LegacySMSService
from Target import ModernNotificationService

class SMSAdapter:
    def __init__(self,modern:ModernNotificationService):
        self.modern=modern

    def send_notification(self, msg):
        self.modern.send_notification(msg)

        