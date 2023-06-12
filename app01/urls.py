from django.urls import path 
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("testpages/", views.testpage01, name='testpage01'),
    path("ChouseisanMaker/", views.ChouseisanMaker, name="CM")
]