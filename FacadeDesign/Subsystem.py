from abc import ABC, abstractmethod
class PayPalGateway:
    def process_payement(self,amount):
        return f"Payement of ${amount} processed via PayPal"

class StripeGateway:
    def Pay(self,amount):
        return f"Payement of ${amount} processed via Stripe"

class CryptoGateway:
    def make_payement(self,amount):
        return f"Payement of ${amount} processed via Crypto(Bitcoin)"
