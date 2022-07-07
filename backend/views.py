from django.shortcuts import render
from .models import Userdata
from .serializers import UserSerializer
from rest_framework import viewsets


# Create your views here.
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Userdata.objects.all()

