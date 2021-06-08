from django.contrib.auth.models import User, Group
from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
