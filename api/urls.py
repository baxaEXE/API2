from django.urls import path, include
from .views import book,custom_user

urlpatterns = [
    path('book/',book),
    path('custom_user/',custom_user),
    path('auth/', include('dj_rest_auth.urls')),
]