from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/<str:username>', profile, name="profile"),
    path('profile/edit/', profile_edit, name="profile_edit"),
]