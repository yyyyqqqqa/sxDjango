from rest_framework import serializers

from role.serializer import RoleModelSerializer

from dept.serializer import DeptModelSerializer
from .models import UserModel, UserRoleModel


class UserModelSerializer(serializers.ModelSerializer):

    dept = DeptModelSerializer()

    class Meta:

        model = UserModel

        fields = "__all__"




class UserRoleModelSerializer(serializers.ModelSerializer):

    users = UserModelSerializer()
    roles = RoleModelSerializer()

    class Meta:

        model = UserRoleModel

        fields = "__all__"
