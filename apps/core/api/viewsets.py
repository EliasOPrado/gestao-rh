from rest_framework import viewsets
from apps.core.api.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer