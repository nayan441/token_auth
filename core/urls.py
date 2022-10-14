from django.urls import path
from .views import RegisterApiView,LoginApiView 


urlpatterns = [
    path('register', RegisterApiView.as_view()),
    path('login', LoginApiView.as_view()),
]