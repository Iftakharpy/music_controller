from django.urls import path

from . import views

urlpatterns = [
    path('<str:message>', views.message),
]