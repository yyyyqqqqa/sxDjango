from django.urls import path

from sxAdmin.user import views

urlpatterns = [
    path('',views.demo)
]