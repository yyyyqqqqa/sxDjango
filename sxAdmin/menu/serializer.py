from rest_framework import serializers

from menu.models import MenuModel


class MenuModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = MenuModel
        fields = '__all__'









