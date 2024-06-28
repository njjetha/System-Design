class DematAccount:
    def __init__(self, name:str, wallet:int,  accountNo:str, bank:str, city:str, state:str, pincode:str):
        self.name=name
        self.wallet=wallet
        self.holding={}
        self.account=Account(accountNo, bank, city, state, pincode)
    
    def getQuaterlyStatement(self):
        res=[]
        pass

class Account:
    def __init__(self, acc, bank, city, state, pincode):
        self.account=acc
        self.bank=bank
        self.city=city
        self.state=state
        self.pincode=pincode

class Stock:
    def __init__(self, company, price, units) :
        self.company=company
        self.price=price
        self.units=units

class StockInventory:
    def __init__(self):
        self.stockListed={}

    def add_stock(self, stock:Stock):
        if stock.company not in self.stockListed:
            self.stockListed[stock.company]=stock
    
    def remove_stock(self, company):
        del self.stockListed[company]
    
class Broker:
    def __init__(self) :
        self.member={}

    
    def add_member(self, name, wallet, accountNo:str, bank:str, city:str, state:str, pincode:str):
        if name not in self.member:
            self.member[name]=DematAccount(
                name, 
                wallet, 
                # holding, 
                accountNo,
                bank,
                city, 
                state,
                pincode)
    
    def buy_stock(self, company, units, name, si:StockInventory):
        user=self.member[name]
        stock=si.stockListed[company]
        if stock.units<units:
            print(f"Can't buy as units not available ")
            return
        stock.units-=units
        user.holding[company]=units
        user.wallet-=stock.price*units 
        print(f"Stock buied {company} successful")

    def update_stock_price(self,company, price,si:StockInventory):
        si[company].price=price
    

if __name__=='__main__':
    broker=Broker()
    si=StockInventory()
    broker.add_member("Neeraj",10000,accountNo="14980", bank="SBI", city="Indore", state="MP", pincode=452009)
    stock=Stock("Bajaj Finance", 6000, 100)
    si.add_stock(stock)
    broker.buy_stock("Bajaj Finance", 2, "Neeraj", si)
