from Facade import PayementFacade

def main():
    facade=PayementFacade()
    print (facade.process_payement(5000,'paypal'))

if __name__=='__main__':
    main()


