from django.contrib.auth.models import User
from rest_framework import serializers
from task.models import Todos



class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)

    class Meta:
        model=User
        fields=["id","username","email","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    

class Todoserializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    due_date=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    class Meta:
        model=Todos
        fields=["id","username","email","password"]