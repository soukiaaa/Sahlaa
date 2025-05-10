from rest_framework import serializers
from sweet_shared.models import sahlaboost
from django.contrib.auth.models import User

class SahlaboostSerializer(serializers.ModelSerializer):
    class Meta:
        model = sahlaboost
        fields = '__all__'

class SignupSerializer(serializers.Serializer):
    name = serializers.CharField()
    domain = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    phonenumber = serializers.CharField()

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Nom d'utilisateur déjà pris.")
        return value

class SigninSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

