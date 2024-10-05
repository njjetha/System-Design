import random
from models import User, Show, ShowSeat, showSeatStatus, Ticket

class BookShowService:
    def create_booking(self, user_id, show_id, show_seat_id):
        if len(show_seat_id)>10:
            raise ValueError("Show seat id must be less than 10")
        try:
            user = User.objects.get(id=user_id)
            if user is None:
                raise User.DoesNotExist
            show = Show.objects.get(id=show_id)
            if show is None:
                raise Show.DoesNotExist
            show_seats = ShowSeat.objects.filter(id__in=show_seat_id)

            for show_seat in show_seats:
                if show_seat.show_seat_status != showSeatStatus.AVAILABLE:
                    raise ValueError('Show Seat status is not Avaialbale')
        
        except:
            raise ValueError("Doesn't exist")
        
        booking = Ticket(
            user = user,
            show = show,
            amount = 100,
            booking_status = "PENDING",
            ticket_number = random.randint(1,9999)
        )

        booking.save()
        
            

        