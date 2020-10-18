from django.conf.urls import url
from . import views

urlpatterns = [
    url('PPTs', views.ebooks, name="sub-ppts"),
]