from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from ecom.models import User, ShippingAddress
from .serializer import UserSerializer, ShippingAddressSerializer, CreateShippingAddressSerializer
from django.shortcuts import get_object_or_404 
from rest_framework.response import Response


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ShippingAddressListCreateAPIView(GenericAPIView):
    serializer_class = CreateShippingAddressSerializer
    def post(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        serializer = CreateShippingAddressSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        shipping_Address = ShippingAddress(
            street = serializer.validated_data["street"],
            city = serializer.validated_data["city"],
            state = serializer.validated_data["state"],
            zip_code = serializer.validated_data["zip_code"],
            country = serializer.validated_data["country"],
            user = user
        )
        shipping_Address.save()
        return Response(ShippingAddressSerializer(shipping_Address).data,status=201)


class ShippingAddressRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer