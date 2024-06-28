from Subsystem import PayPalGateway, StripeGateway, CryptoGateway

class PayementFacade:
    def __init__(self):
        self._paypal=PayPalGateway()
        self._stripe=StripeGateway()
        self._crypto=CryptoGateway()

    def process_payement(self, amount, gateway):
        if gateway=='paypal':
            return self._paypal.process_payement(amount)
        if gateway == 'stripe':
            return self._stripe.Pay(amount)
        if gateway == 'crypto':
            return self._crypto.make_payement(amount)