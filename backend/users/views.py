from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserDetailsSerializer

User = get_user_model()

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]
