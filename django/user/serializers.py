from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()

    class Meta:
        model = User
        fields = '__all__'