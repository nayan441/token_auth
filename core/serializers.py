
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import Channel, Org, User



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        depth = 1
        exclude = ("is_staff","is_active", "is_superuser", "last_login","groups", "user_permissions")
        extra_kwargs = {
            "password":{"write_only":True}
        }
    def create(self, validate_data):
        password = validate_data.pop('password', None)
        instance = self.Meta.model(**validate_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class OrgSerializer(ModelSerializer):
    class Meta:
        model = Org
        fields = "__all__"
        depth = 1

class ChannelSerializer(ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"
        depth = 1