from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.loginview,name='login'),
    path('logout/',views.logoutview,name='logout'),
    path('tasks/',views.tasks,name='tasks'),
]