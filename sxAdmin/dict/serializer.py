from rest_framework import serializers

from dict.models import DictTypeModel, DictDataModel



class DictTypeModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = DictTypeModel

        fields = "__all__"

class DictDataModelSerializer(serializers.ModelSerializer):


    class Meta:

        model = DictDataModel

        fields = "__all__"



