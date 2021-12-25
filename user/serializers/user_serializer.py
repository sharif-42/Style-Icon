from rest_framework import serializers
from user.models import User


class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "mid_name",
            "email",
            "phone_number",
        ]
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 5},
        }


class UserOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "uuid",
            "username",
            "first_name",
            "last_name",
            "mid_name",
            "email",
            "phone_number",
            "is_dashboard_user",
        ]
