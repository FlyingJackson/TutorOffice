from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)
from django.contrib.auth.views import (
    PasswordResetDoneView, PasswordResetCompleteView
)

router = routers.DefaultRouter()
router.register('register', RegisterView, basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('auth/user-activate/<str:token>/', ActivateUserView.as_view(), name='activate'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]
