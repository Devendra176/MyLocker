from email.mime import base
from posixpath import basename
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import RegisterViaPhoneView, OtpVerificationView

# Create a router and register our viewsets with it.
UserRouter = DefaultRouter()
UserRouter.register(r'^register', RegisterViaPhoneView, basename='phone')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('register/', RegisterViaPhoneView.as_view(), name='register_method'),
    path('verification/', OtpVerificationView.as_view(), name='verfication_method')
]
# urlpatterns = UserRouter.urls
