
from djoser.views import (
    UserViewSet,
    TokenCreateView,
)

from django.urls import path



urlpatterns = [
    # User endpoints
    path('', UserViewSet.as_view({'post': 'create'}), name='user-create'),
    path('me/', UserViewSet.as_view({'get': 'current_user'}), name='user-current'),
    path('<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='user-detail'),
    
    # ... your other endpoints ...
    path("resend-activation/", UserViewSet.as_view({"post": "resend_activation"}), name="resend_activation"),
    path("activation/<str:uid>/<str:token>/", UserViewSet.as_view({"post": "activate"}), name="activate"),
    path("reset-password/", UserViewSet.as_view({"post": "reset_password"}), name="reset_password"),
    path("reset-password-confirm/<str:uid>/<str:token>/", UserViewSet.as_view({"post": "reset_password_confirm"}), name="reset_password_confirm"),
]