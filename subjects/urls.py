from django.conf.urls import url
from . import views

urlpatterns = [
    url('CBNSM', views.cbnsm, name = 'CBNSM'),
    url('COA', views.coa, name = 'COA'),
    url('MFCS', views.mfcs, name = 'MFCS'),
    url('PM', views.pm, name = 'PM'),
    url('PM-Lab', views.pmlab, name = 'PM-Lab'),
    url('DataFileAndStructures', views.ds, name = 'DataFileAndStructures'),
    url('Java-Lab', views.javalab, name = 'Java-Lab'),
    url('ObjectOrientedProgramming', views.oop, name = 'ObjectOrientedProgramming'),
    url('OperatingSystem', views.os, name = 'OperatingSystem'),
    url('SoftwareEngineering', views.se, name = 'SoftwareEngineering'),
    url('ComputerNetworks', views.cn, name = 'ComputerNetworks'),
    url('DBMS-Lab', views.dbmslab, name = 'DBMS-Lab'),
    url('DatabaseManagementSystem', views.dbms, name = 'DatabaseManagementSystem'),
    url('InternetTechnology', views.it, name = 'InternetTechnology'),
    url('TheoryofComputation', views.toc, name = 'TheoryofComputation'),
    url('Algorithms', views.algo, name = 'Algorithms'),
    url('CommunicationSkills(Lab)', views.cskill, name = 'CommunicationSkills(Lab)'),
    url('ComputerGraphicsandVisualization', views.cg, name = 'ComputerGraphicsandVisualization'),
    url('DataWarehousing', views.dw, name = 'DataWarehousing'),
    url('IntroductiontoAI', views.ai, name = 'IntroductiontoAI'),
    url('InformationSystemsManagement', views.ism, name = 'InformationSystemsManagement'),
    url('Projects', views.project, name = 'Projects'),
]