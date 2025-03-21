from django.urls import path
from profiles.views import home,dashboard
urlpatterns = [
    path('',home, name='home' ),
    path('dashboard',dashboard, name='dashboard' ),
]
