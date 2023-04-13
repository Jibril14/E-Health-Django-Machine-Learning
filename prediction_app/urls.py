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
    path(
        'check/result/',
        views.diabetes_result,
        name="diabetes_result"),
    path(
        'download/result/',
        views.download,
        name="download"),
]
