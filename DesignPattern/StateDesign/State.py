# Step 1: Define the State Interface
class CheckoutState:
    def add_item(self, item):
        pass

    def review_cart(self):
        pass

    def enter_shipping_info(self, info):
        pass

    def process_payment(self):
        pass