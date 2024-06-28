from ConcreteState import CheckoutContext
if __name__ == "__main__":
    cart = CheckoutContext()

    cart.add_item("Product 1")
    cart.review_cart()
    cart.enter_shipping_info("123 Main St, City")
    cart.process_payment()