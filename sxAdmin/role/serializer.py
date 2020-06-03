from rest_framework import serializers

from role.models import RoleModel

from role.models import RoleMenuModel

from menu.serializer import MenuModelSerializer


class RoleModelSerializer(serializers.ModelSerializer):


    class Meta:

        model = RoleModel

        fields = "__all__"


class RoleMenuModelSerializer(serializers.ModelSerializer):
    role = RoleModelSerializer()
    menu = MenuModelSerializer()

    class Meta:

        model = RoleMenuModel
        fields = "__all__"



