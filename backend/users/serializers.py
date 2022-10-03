import re
from datetime import datetime, timezone

from django.db import transaction
from django.contrib.auth.hashers import make_password, check_password

from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import UserDetailsSerializer

from users.models import CustomUser, UserProfile


Pattern = re.compile("(0|91)?[6-9][0-9]{9}$")



class CustomRegisterSerializer(RegisterSerializer):
    phone = serializers.CharField(max_length=30)
    
    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.phone = self.data.get('phone')
        user.save()
        return user


class PhoneRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone']

    def validate(self, data):
        phone = data.get('phone')
        if not Pattern.match(phone):
            raise serializers.ValidationError("Not matches")
        return data

    
    def save(self, **kwargs):
        phone = self.validated_data['phone']
        otp = kwargs['otp']
        otp = make_password(str(otp))
        user = CustomUser.objects.filter(phone=phone)
        if user.exists():
            user.update(otp=otp, created_at = datetime.now(tz=timezone.utc))
        else:
            user = CustomUser.objects.create(username=phone, phone=phone, otp=otp)
            user.save()
        return user



class OtpVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone', 'otp']

    def validate(self, data):

        current_time = datetime.now(timezone.utc)
        phone = data.get('phone')
        otp = data.get('otp')
        user = CustomUser.objects.filter(phone=phone).first()

        if not Pattern.match(phone):
            raise serializers.ValidationError("Not matches")

        elif not CustomUser.objects.filter(phone=phone).exists():
            raise serializers.ValidationError("user not found")

        elif not check_password(otp, user.otp):
            user.mobile_verified = False
            user.save()
            raise serializers.ValidationError("Otp not matched")

        elif (current_time - user.created_at).seconds > 300:
            user.mobile_verified = False
            user.save()
            raise serializers.ValidationError("Otp expired")

        return data
    
    def update(self, instance, **kwargs):
        mobile_verified = kwargs.get('mobile_verified')
        instance.mobile_verified = mobile_verified
        instance.save()
        return instance


class UserProfileData(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'



class CustomUserDetailsSerializer(UserDetailsSerializer):
    profile = UserProfileData(source='user_profile_data', many=False)

    class Meta:
        model = CustomUser
        fields = ('pk', 'phone', 'email', 'username', 'is_active', 'is_staff', 'profile')
        read_only_fields = ('email',)