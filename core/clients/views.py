from django.shortcuts import Http404, get_object_or_404, redirect
from django.urls import reverse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import (CreateModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import RegisterSerializer, ProfileSerializer
from .services import Email

# Create your views here.


class RegisterView(CreateModelMixin, GenericViewSet):
    """
    Регистрация пользователя и отправка
    сообщения для верификации почты
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = get_object_or_404(User, pk=response.data['id'])
        token = RefreshToken.for_user(user)
        return Email.send_email(request, user, token)


class ActivateUserView(RetrieveAPIView):
    """Подтверждение верификации и перенаправление на профиль"""

    def get(self, request, token, *args, **kwargs):
        try:
            # по refresh-токену проверяет валидность(срок) и идентифицирует
            user_id = RefreshToken(token).payload['user_id']
            user = get_object_or_404(User, pk=user_id)
            if not user.is_active:
                user.is_active = True
                user.save()
                token = RefreshToken.for_user(user)
                response = redirect(reverse('profile'))
                response.set_cookie('access_token', str(token.access_token), httponly=True)
                response.set_cookie('refresh_token', str(token), httponly=True)
                return response
            return Response({"ERROR": "Ссылка больше недействительна!"},
                            status=status.HTTP_400_BAD_REQUEST)
        except TokenError as error:
            return Response({'ERROR': "Данная ссылка не является действительной! Возможно срок её действия истёк."},
                            status=status.HTTP_400_BAD_REQUEST)
        except (ValueError, TypeError, User.DoesNotExist, KeyError):
            return Http404


class ProfileViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
