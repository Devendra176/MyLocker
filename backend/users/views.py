from email import message
import random

from django.contrib.auth import login

from rest_framework import status
from rest_framework.authtoken.models import Token

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.models import CustomUser

from users.serializers import PhoneRegisterSerializer, OtpVerificationSerializer
from common.response import ResponseGenerator




# Create your views here.


class RegisterViaPhoneView(generics.CreateAPIView):
    """Registration using phone number.

    returns OTP for a phone number.
    """
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PhoneRegisterSerializer

    def post(self, request, *args, **kwargs):
        status_code = status.HTTP_400_BAD_REQUEST
        message = None
        is_valid = False
        
        data = request.data
        serializer = PhoneRegisterSerializer(data=data)

        if serializer.is_valid():
            is_valid = True
            status_code = status.HTTP_200_OK
            otp = random.randint(1000,9999)
            user = serializer.save(otp = otp)
            data = {'phone': data.get('phone'), 'otp': otp}
            message = 'Succeess'
        
        return ResponseGenerator(data=data, status=status_code, is_valid=is_valid, message=message, errors=serializer.errors)

class OtpVerificationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = OtpVerificationSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = OtpVerificationSerializer(data=data)

        is_valid = False
        status_code = status.HTTP_400_BAD_REQUEST
        message = 'Otp not matched'

        if serializer.is_valid():
            is_valid = True
            status_code = status.HTTP_200_OK
            message = 'Login successfully'

            instance = CustomUser.objects.get(phone=data.get('phone'))
            serializer.update(instance, mobile_verified = True)
            token, create = Token.objects.get_or_create(user=instance)
            login(request, instance)

            data = {'token': token.key}

        return ResponseGenerator(data=data, status=status_code, is_valid=is_valid, message=message, errors=serializer.errors)