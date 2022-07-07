from backend.models import Userdata
from rest_framework import serializers

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Userdata
        # fields = '__all__'
        fields = ['id','name','email','phone','dob','gender','department','course']
