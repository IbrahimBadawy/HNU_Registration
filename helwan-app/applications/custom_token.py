# 📁 applications/custom_token.py

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_admin"] = user.is_admin
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data["is_admin"] = self.user.is_admin
        return data


class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
