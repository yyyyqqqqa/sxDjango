from rest_framework import serializers

from sxAdmin.user.serializer import UserModelSerializer
from sxCustomer.stu.models import StuModel, StatusModel, StuDetailModel



class StatusModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = StatusModel

        fields = "__all__"

class StuModelSerializer(serializers.ModelSerializer):

    status = StatusModelSerializer()
    gw = UserModelSerializer()

    class Meta:

        model = StuModel

        fields = "__all__"




class StuDetailModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = StuDetailModel

        fields = "__all__"
