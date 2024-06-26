import datetime


class Cinema:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super(Cinema, cls)
        return cls._instance
    

class CinemaHall:
    def __init__(self, name, number_of_seats):
        self.name=name
        self.seats=[CinemaHallSeats(i) for i in range(1,number_of_seats+1)]
        self.shows=[]

    def add_shows(self,show):
        self.shows.append(show)

class CinemaHallSeats:
    def __init__(self, seat_number):
        self.seat_number=seat_number
        self.is_reserved=False

class Show:
    def __init__(self, movie, cinema_hall, start_time, end_time):
        self.movie=movie
        self.cinema_hall=cinema_hall
        self.start_time=start_time
        self.end_time=end_time
        self.show_seats=[ShowSeat(cinema_hall_seat) for cinema_hall_seat in cinema_hall.seats ]

    def reserveSeat(self, seat_number):
        if seat_number <=len(self.show_seats) and not self.show_seats[seat_number-1].cinema_hall_seat.is_reserved:
            self.show_seats[seat_number-1].cinema_hall_seat.is_reserved=True
            return True
        return False

class ShowSeat:
    def __init__(self, cinema_hall_seat):
        self.cinema_hall_seat=cinema_hall_seat

class Booking:
    def __init__(self, show, seat):
        self.booking_number=f"{datetime.now().timestamp()}"
        self.show=show
        self.seat=seat
        self.status="Booked"
    def make_payement(self, amount):
        payment=Payment(amount)
        payment.process_payment()
        return payment

class Payment:
    def __init__(self, amount):
        self.amount= amount
        self.status="Pending"
    
    def process_payment(self):
        self.status="Completed"

class Notification:
    @staticmethod
    def send_notification(message):
        print(f"Notification: {message}")


class Account:
    def __init__(self, username, password, accounttype):
        self.username=username
        self.password=password
        self.accounttype=accounttype
        