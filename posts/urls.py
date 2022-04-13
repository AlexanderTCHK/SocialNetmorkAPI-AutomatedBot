from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostCreateView.as_view()),
    path('<int:pk>/like/create/', views.PostLikeCreateView.as_view()),
    path('<int:pk>/like/delete/', views.PostLikeDeleteView.as_view()),
    path('analytics/', views.PostLikesAnalyticsView.as_view()),
]
