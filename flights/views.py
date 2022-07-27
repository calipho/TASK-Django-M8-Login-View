import datetime

from rest_framework import generics

from flights import serializers
from flights.models import Booking, Flight, User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class FlightsList(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = serializers.FlightSerializer


class BookingsList(generics.ListAPIView):
    serializer_class = serializers.BookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(date__gte=datetime.date.today())


class BookingDetails(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingDetailsSerializer
    lookup_url_kwarg = "booking_id"


class UpdateBooking(generics.RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = serializers.UpdateBookingSerializer
    lookup_url_kwarg = "booking_id"


class CancelBooking(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    lookup_url_kwarg = "booking_id"


class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserRegistrationSerializer


class LoginUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserLoginSerializer

    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(user)
