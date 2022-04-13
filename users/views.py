from rest_framework.response import Response
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializers import (UserRegisterSerializer,
                          CustomTokenSerializer,
                          UserSerializer,
                          UserActivitySerializer,
                          )
from .models import User
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView


class UserRegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = {
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        }
        return Response(data,
                        status=status.HTTP_201_CREATED)


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer


class UseActivityView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserActivitySerializer
