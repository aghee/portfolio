from django.urls import path
from .import views

urlpatterns=[
    path("",views.home,name="home"),
    path("webdev/",views.home,name="home"),
    path("contact/",views.contact, name="contact"),
    path("about/",views.about, name="about"),
    path("project/<int:id>/",views.project,name="project"),
    path("dataprojects/",views.dataprojects,name="dataprojects"),
    path("dproject/<int:pk>/",views.dproject,name="dproject"),
    
]