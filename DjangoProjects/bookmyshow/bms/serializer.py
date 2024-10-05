from rest_framework import serializers

class CreateBookingRequestDto(serializers.Serializer):
    user_id = serializers.IntegerField()
    show_id = serializers.IntegerField()
    show_seats_id = serializers.ListField(child=serializers.IntegerField())



class CreateBookingResponseDto(serializers.Serializer):
    booking_id = serializers.IntegerField(required = False)
    reponse_stauts = serializers.CharField(required = False)
