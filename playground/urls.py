from django.urls import path
from . import views

#URLConfiuration
urlpatterns = [
    path('hello/', views.say_hello)
]
