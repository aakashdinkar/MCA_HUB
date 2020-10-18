from django.conf.urls import url
from . import views

urlpatterns = [
    url('QuestionPapers', views.ebooks, name="sub-questionpapers"),
]