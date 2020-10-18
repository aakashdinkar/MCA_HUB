from django.conf.urls import url
from . import views

urlpatterns = [
    url('sem1', views.sem1, name = 'sem-1'),
    url('pm', views.pm, name = 'sem-pm'),
    url('coa', views.coa, name = 'sem-coa'),
    url('mfcs', views.mfcs, name = 'sem-mfcs'),
    url('cbnsm', views.cbnsm, name = 'sem-cbnsm'),
    url('PmLab', views.pmlab, name = 'sem-pmlab'),
]