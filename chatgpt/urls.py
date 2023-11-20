from django.urls import path
from chatgpt import views

urlpatterns = [
    path("", views.chat, name="chat"),
]
