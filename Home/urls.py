from django.conf.urls import url
from . import views

urlpatterns = [
    url('Home', views.index, name="main-homepage")
]