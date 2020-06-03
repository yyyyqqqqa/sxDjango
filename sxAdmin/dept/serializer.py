from rest_framework import serializers

from dept.models import DeptModel


class DeptModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = DeptModel

        fields = "__all__"