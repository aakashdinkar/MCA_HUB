from django.conf.urls import url
from . import views

urlpatterns = [
    url('Upload', views.upload, name="upload-page"),
]