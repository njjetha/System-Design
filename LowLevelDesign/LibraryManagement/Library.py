from abc import ABC
import uuid


class Library:
    def __init__(self, name, address):
        self.name=name
        self.address= address
        self.account=[]
        self.catalog=Catalog()
    
    def add_account(self,acc):
        self.account.append(acc)

class Account(ABC):
    def __init__(self, name, accountId):
        self.name=name
        self.accountId=accountId
        self.libraryCard=LibraryCard(self)

class Librarian(Account):
    def add_book(self, library:Library, book):
        library.catalog.add_book(book)

class Member(Account):
    def __init__(self, name, accountId):
        super().__init__(name, accountId)
        self.checkout_books=[]

class Book:
    def __init__(self, isbn, title, subject, publisher, authors) :
        self.isbn=isbn
        self.title=title
        self.subject=subject
        self.publisher=publisher
        self.authors=authors
        self.book_item=[]
    def add_book(self, book_item):
        self.book_item.append(book_item)

class BookItem:
    def __init__(self, barcode, book:Book, rack):
        self.barcode=barcode
        self.book=book
        self.rack=rack
        self.reserved=False

class BookReservation:
    def __init__(self) -> None:
        self.resrvation={}
    def reserve_book(self, book_item:BookItem, member):
        if book_item.reserved==False:
            book_item.reserved=True
            self.resrvation[book_item.barcode]=member
            print(f"Book Reservation Successful")
            return True
        print("Book is already Resrved")
        return False
        
class Catalog:
    def __init__(self):
        self.book_by_title={}
    def add_book(self, book:BookItem):
        title=book.book.title
        if  title not in self.book_by_title:
            self.book_by_title[title]=[]
        self.book_by_title[title].append(book)
    def search_by_title(self, title):
        return self.book_by_title.get(title,[])

class LibraryCard:
    def __init__(self,acc) :
        self.acc=acc
        self.card_num=get_card_number()
        
def get_card_number():
    return str(uuid.uuid4())


if __name__=="__main__":
    library=Library("Central Library", "123 Library st")
    
    librarian=Librarian("Joe Doe",1)
    library.add_account(librarian)
    
    member=Member("Jane Smith", 2)
    library.add_account(member)

    book=Book("123", "Tht", "Fiction", "Scb", ["Neeraj"])
    rack="Rack1"
    book_item=BookItem("BC!@#", book, rack)

    librarian.add_book(library, book_item)

    book_res=BookReservation()
    fb=library.catalog.search_by_title("Tht")
    if fb:
        book_res.reserve_book(fb[0], member)
    else:
        print(f"Book not Found")