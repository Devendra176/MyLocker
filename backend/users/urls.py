from django.urls import path

from users.views import RegisterViaPhoneView, OtpVerificationView


urlpatterns = [
    path('register/', RegisterViaPhoneView.as_view(), name='register_method'),
    path('verification/', OtpVerificationView.as_view(), name='verfication_method')
]
