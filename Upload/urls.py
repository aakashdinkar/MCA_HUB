from django.conf.urls import url
from . import views
from MCA_HUB import settings
from django.conf.urls.static import static

urlpatterns = [
    url('Upload', views.upload, name="upload-page"),
]
