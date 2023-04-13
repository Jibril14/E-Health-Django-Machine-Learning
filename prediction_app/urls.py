from django.urls import path
from prediction_app import views

urlpatterns = [
    path(
        '',
        views.index,
        name="home"),
    path(
        'check/diabetes/',
        views.diabetes_prediction,
        name="diabetes_prediction"),
]
