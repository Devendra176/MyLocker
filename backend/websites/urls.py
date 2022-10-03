from importlib.resources import path
from django.urls import re_path
from backend.websites.views import WebsitesDataView, WebsitesAddDataView

urlpatterns = [
    re_path(r'^data/$', WebsitesDataView.as_view(), name='get_user_website_data'),
    re_path(r'^add/$', WebsitesAddDataView.as_view(), name='add_website_data')
]