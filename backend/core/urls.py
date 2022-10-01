"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

from django.conf import settings #add this
from django.conf.urls.static import static 

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", RedirectView.as_view(url="/swagger")),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('accounts/', include('allauth.urls')),

    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    
    re_path(r'^phone/', include('users.urls')),
    re_path(r'^website/', include('websites.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
