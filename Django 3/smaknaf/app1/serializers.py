from django import serializers
from .models import users

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ['id','FName','LName','age','place','email','password']