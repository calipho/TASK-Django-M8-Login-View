from rest_framework import serializers

from .models import Booking, Flight, User


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["destination", "time", "price", "id"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["flight", "date", "id"]


class BookingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["flight", "date", "passengers", "id"]


class UpdateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["date", "passengers"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        password = validated_data.pop('password')
        newuser = User(**validated_data)
        newuser.set_password(password)
        newuser.save()

        return validated_data


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


def validate(self, data):
    user = data.get('username')
    password = data.get('password')

    try:
        user = User.objects.get(username=user)
    except User.DoesNotExist:
        raise serializers.ValidationError("User does not exist")

    if not user.check_password(password):
        raise serializers.ValidationError("Incorrect password")
