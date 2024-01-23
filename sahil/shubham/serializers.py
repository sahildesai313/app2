from django.contrib.auth.models import Group,User
from rest_framework import serializers



class Userserializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model =User
        Filed=['url','username','email','groups']
        
        
        
        
class Groupserializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model=Group
        Field=['url','username']