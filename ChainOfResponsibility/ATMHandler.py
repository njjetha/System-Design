# from abc import ABC
class CashWithdrawal:
    def __init__(self, amount):
        self.amt_withdraw=amount

class CashRequestHandler:
    def __init__(self, successor=None):
        self.successor=successor
    def handleRequest(self, amt1:CashWithdrawal):
        if self.successor:
            self.successor.handleRequest(amt1)

class FivehunderedNotes(CashRequestHandler):
    def __init__(self,notes, obj:CashRequestHandler):
        # super().__init__(obj)
        self.obj=obj
        self.notes=notes
    def handleRequest(self,amt1:CashWithdrawal):
        cnt=0
        
        while(amt1.amt_withdraw>=500 and self.notes):
            amt1.amt_withdraw-=500
            cnt+=1
            self.notes-=1

        print(f"Total 500 rupess Notes ", cnt)
        super().__init__(self.obj)
        super().handleRequest(amt1)  
class TwoHundredNotes(CashRequestHandler):
    def __init__(self,notes, obj:CashRequestHandler):
        # super().__init__(obj)
        self.obj=obj
        self.notes=notes
    def handleRequest(self,amt1:CashWithdrawal):
        # amt=amt1.amt_withdraw
        cnt=0
        while(amt1.amt_withdraw>=200 and self.notes):
            amt1.amt_withdraw-=200
            cnt+=1
            self.notes-=1
        print(f"Total 200 rupess Notes ", cnt)
        super().__init__(self.obj)
        super().handleRequest(amt1)  
class OneHundredNotes(CashRequestHandler):

    def __init__(self,notes, obj:CashRequestHandler):
        # super().__init__(obj)
        self.obj=obj
        self.notes=notes
    def handleRequest(self,amt1:
                      CashWithdrawal):
        
        cnt=0
        while(amt1.amt_withdraw>=10 and self.notes):
            amt1.amt_withdraw-=100
            cnt+=1
            self.notes-=1
        print(f"Total 100 rupess Notes ", cnt)
        super().__init__(self.obj)
        super().handleRequest(amt1)  

if __name__=="__main__":
    totalCashWithdraw=CashWithdrawal(4000)
    one=OneHundredNotes(50,None)
    two=TwoHundredNotes(60,one)
    five=FivehunderedNotes(2,two)
    five.handleRequest(totalCashWithdraw)
    
    
        
        
