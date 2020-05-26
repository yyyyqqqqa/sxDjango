from django.urls import path

from sxAdmin.user import views

urlpatterns = [
    path('getToken',views.LoginView.as_view())
]