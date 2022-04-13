from django.urls import path
from . import views

urlpatterns = [
    path('', views.UsersListView.as_view()),
    path('register/', views.UserRegisterView.as_view()),
    path('<int:pk>/user_activity/', views.UseActivityView.as_view()),
]
