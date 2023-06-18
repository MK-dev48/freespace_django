from django.urls import path 
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("testpage01/", views.testpage01, name='testpage01'),
    path("ChouseisanMaker/", views.ChouseisanMaker, name="CM"),
    path("testpage02/", views.testpage02, name='tp02'),
    path("testpage03/", views.testpage03, name='tp03'),
    path("testpage04/", views.testpage04, name='tp04'),
]   