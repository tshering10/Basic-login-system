from django.urls import path
from accounts.views import Signup_view

urlpatterns = [
    path('signup/', Signup_view.as_view(), name='signup'),
]
