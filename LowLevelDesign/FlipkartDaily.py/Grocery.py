import threading

class Item:
    def __init__(self, category, brand, price):
        self.category=category
        self.brand=brand
        self.price=price
        self.quantity=0

    def __repr__(self):
        return f"{self.category} -> {self.brand} ->{self.price} -> {self.quantity}"
    

class Inventory:
    def __init__(self):
        self.items = {}
        self.lock= threading.lock()
    
    def set_price(self, category, brand, price):
        with self.lock():
            key=(category, brand)
            if key not in self.items:
                self.items[key]=Item(category, brand, price)
            else:
                self.items[key].price=price
    
    def add_item(self, category, brand, quantity):
        with self.lock():
            key=(category, brand)
            if key not in self.items:
                return f"set the price of item first"
            else:
                self.items[key].quantity+=quantity
    
    def search(self, **filters):
        results=[]
        for item in self.items.values():
            match= True
            print(item)
            for key, value in filter.items():
                print(key, value)
                if getattr(item,key) !=value:
                    match=False
                    break
            if match:
                results.append(item)
        return results

    def __repr__(self) -> str:
        with self.lock:
            return '\n'.join(str(item) for item in self.items.values())

class Cart:
    def __init__(self):
        self.item={}
        self.total_price=0
    
    def add_item(self, item, quantity):
        key=(item.category, item.brand)
        if key in self.items:
            self.items[key]['quantity']+=quantity
        else:
            self.items[key]={'items':item, 'quantity':quantity}
        self.total_price+=item.price*quantity
    
    def remove_item(self, item, quantity):
        key=(item.category, item.brand)
        if key in self.items:
            self.items[key]['quantity']-=quantity
            if self.items[key]['quantity']<=0:
                del self.item[key]
            self.total_price-=item.price*quantity

    def __repr__(self):
        return '\n'.join(f"{item['item'].brand} -> {item['item'].category} -> {item['quantity']} -> Total price: {self.total_price}" for item in self.item.values())

class User:
    def __init__(self, name, address, amount):
        self.name=name
        self.address=address
        self.amount=amount
        self.cart=Cart()
        self.lock=threading.Lock()
    
    def add_to_wallet(self,amount):
        self.amount+=amount

    def __repr__(self):
        return f"{self.name} -> Wallet: {self.amount} \n Cart:{self.cart}"

class Store:
    def __init__(self):
        self.inventory=Inventory()
        self.users={}
        self.lock=threading.Lock()

    def add_user(self, name, address, wallet_amount):
        with self.lock:
            self.users[name]=User(name, address, wallet_amount)
    
    def add_to_cart(self, username, category, brand, quantity):
        with self.lock:
            user = self.users.get(username)
            if not user:
                return f"User not found"

            key = (category, brand)
            item=self.inventory.items.get(key)
            if not item:
                return f"{brand} {category} not found"
            if item.quantity<quantity:
                return f"Not enough quantity for brand available {item.quantity}"

            with user.lock:
                item.quantity-=quantity
                user.cart.add_items(item,quantity)

    def remove_from_cart(self, username, category, brand, quantity):
        with self.lock:
            user=self.users.get(username)
            if not user:
                return f"No such user found"
            key=(category, brand)
            item = self.inventory.items.get(key)

            if not item:
                return f" Item {brand} -> {category} not found"

            with user.lock:
                user.cart.remove_item(item,quantity)
                item.quantity+=quantity

    def checkout(self, username):
        with self.lock:
            user=self.users.get(username)
            if not user:
                return f"User {username} not found"
            
            with user.lock:
                if user.wallet_amount< user.cart.total_price:
                    return f"Insufficient amount"

                user.wallet_amount-=user.cart.total_price
                print("Amount available in cart", {user.wallet_amount})
                user.cart=Cart()
    
    def search_item(self, **filters):
        result=self.inventory.search(**filter)
        for item in result:
            print(item)
    
def main():
    store=Store()

    store.inventory.set_price("Milk", "Amul", 100)
    store.inventory.set_price("Curd", "Amul", 50)
    store.inventory.set_price("Milk", "Nestle", 60)
    store.inventory.set_price("Curd", "Nestle", 90)

    store.inventory.add_item("Milk", "Amul", 100)
    store.inventory.add_item("Curd", "Amul", 100)
    store.inventory.add_item("Milk", "Nestle", 100)
    store.inventory.add_item("Curd", "Nestle", 100)

    store.add_user("Jhonny", "Flipkart Bellandur", "Bangalore", 600)
    store.add_to_cart("Jhonny", "Milk", "Nestle", 5)

    print(store.users["Jhonny"].cart)

    store.checkout("Jhonny")