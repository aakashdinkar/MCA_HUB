from django.conf.urls import url
from . import views

urlpatterns = [
    url('Practicals', views.ebooks, name="sub-practicals"),
]