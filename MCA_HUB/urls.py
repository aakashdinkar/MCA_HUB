from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from Home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', views.index),
    url('', include('subjects.urls')),
    url('', include('Ebooks.urls')),
    url('', include('Notes.urls')),
    url('', include('PPTs.urls')),
    url('', include('Practicals.urls')),
    url('', include('QuestionPapers.urls')),
]
