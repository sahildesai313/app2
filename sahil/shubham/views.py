from django.contrib.auth.models import User,Group
from rest_framework import permissions,viewsets
from.serializers import Userserializer,Groupserializer




class Userviewset(viewsets.ModelViewSet):
    x= User.objects.all()
    serializer_class= Userserializer
    permission_classes=[permissions.IsAuthenticated]
    
    
    
class Groupviewset(viewsets.ModelViewSet):
    y=Group.objects.all()
    serializer_class=Groupserializer
    permission_classes=[permissions.IsAuthenticated]