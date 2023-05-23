from django.urls import include, re_path as url,path
from .views import *

app_name = 'url_short_app'


urlpatterns = [
    path("short_url/", UrlConverterView.as_view(), name="login"),
]
