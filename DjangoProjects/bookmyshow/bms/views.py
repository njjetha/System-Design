from typing import Any
from django.shortcuts import render
from rest_framework import viewsets
from bms.serializer import CreateBookingRequestDto,CreateBookingResponseDto
from service import BookShowService

# Create your views here.
class BookingViewSet(viewsets.ViewSet):

    def __init__(self, service:BookShowService, **kwargs: Any) -> None:
        self.service = service
        super().__init__(**kwargs)


    def create_booking(self,request):
        
        try:
            req = CreateBookingRequestDto(request.data)
            req.is_valid(raise_exception=True)
            booking = self.service.create_booking(
                user_id=req.data.get("user_id"),
                show_id=req.data.get("show_id"),
                show_seat_id=req.data.get("show_seat_ids")
            )

            data = {
                "booking_id": booking.id,
                "response_status": booking.booking_status,
            }

            val = CreateBookingResponseDto(data = data)
            val.is_valid(raise_exception=True)
            return val.data

        except Exception as e:
            print(e)
            return CreateBookingResponseDto(data = {"response_status":"FAILED"}).data