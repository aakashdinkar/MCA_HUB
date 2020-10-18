from django.conf.urls import url
from . import views

urlpatterns = [
    url('Notes', views.ebooks, name="sub-notes"),
]