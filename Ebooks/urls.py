from django.conf.urls import url
from . import views

urlpatterns = [
    url('EBooks', views.ebooks, name="sub-ebooks"),
]