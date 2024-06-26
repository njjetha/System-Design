from Context import EmptyCartState

class CheckoutContext:
    def __init__(self):
        self.current_state = EmptyCartState()

    def add_item(self, item):
        self.current_state = self.current_state.add_item(item)

    def review_cart(self):
        self.current_state = self.current_state.review_cart()

    def enter_shipping_info(self, info):
        self.current_state = self.current_state.enter_shipping_info(info)

    def process_payment(self):
        self.current_state.process_payment()