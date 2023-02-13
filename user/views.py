from django.contrib.auth import authenticate, login

from rest_framework import generics, status, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer, LogInSerializer

# Create your views here.


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Successfully signed-up', status=status.HTTP_201_CREATED)


def get_login_response(user, request):
    refresh = RefreshToken.for_user(user)
    data = {
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token)
    }
    return data


class LogInAPIView(generics.GenericAPIView):
    serializer_class = LogInSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=serializer.validated_data.get('email'),
                            password=serializer.validated_data.get('password'))
        if not user:
            raise exceptions.AuthenticationFailed
        login(request, user)
        return Response(data=get_login_response(user, request))
