from django.urls import path
from account import views

urlpatterns = [ 
     path('user/register/', views.register, name="register"),
     path('user/login/', views.login, name="login"),
     path('user/logout/', views.logout, name="logout"),    
     path('doctors/', views.doctors, name="doctors"), 
     path('profile/', views.profile, name="profile"),    
]

