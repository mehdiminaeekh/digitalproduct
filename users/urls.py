from django.urls import path

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

from .views import RegisterView, Get_Token_View


urlpatterns = [
    path('register/', RegisterView.as_view()),
    # path('get-token/', Get_Token_View.as_view()),

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


