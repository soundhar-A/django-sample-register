from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=250)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=250)
    confirm_password = serializers.CharField(max_length=250)
