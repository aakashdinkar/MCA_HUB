from django.conf.urls import url
from . import views
from MCA_HUB import settings
from django.conf.urls.static import static

urlpatterns = [
    url('Upload', views.upload, name="upload-page"),
]

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
