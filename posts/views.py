from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .filters import LikesFilter
from .models import Post, Like
from .serializers import (PostCreate,
                          LikeSerializer,
                          LikeAnalyticsSerializer)


class PostCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreate

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostLikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def post(self, request, *args, **kwargs):
        author = self.request.user
        pk = kwargs.get('pk')
        serializer = self.get_serializer(
            data={'author': author.pk, 'post': pk})
        print(serializer)
        serializer.is_valid(raise_exception=True)
        post = Post.objects.get(pk=pk)
        post.likes.add(author)
        data = serializer.data
        return Response(data,
                        status=status.HTTP_201_CREATED)


class PostLikeDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def delete(self, request, **kwargs):
        author = request.user
        pk = kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        post.likes.remove(author)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostLikesAnalyticsView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeAnalyticsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LikesFilter
    permission_classes = [AllowAny]
    def get_queryset(self):
        data = self.queryset
        data = self.queryset.extra(
            select={'date': "date(liked_date)"})
        data = self.queryset.extra(
            select={'date': "date(liked_date)"}).values(
            'date')
        data = self.queryset.extra(
            select={'date': "date(liked_date)"}).values(
            'date').annotate(likes=Count('pk'))
        return data
