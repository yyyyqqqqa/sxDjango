from rest_framework import serializers

from sxAdmin.user.models import StudentModel,GradeModel



class GradeModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = GradeModel

        fields = "__all__"


class StudentModelSerializer(serializers.ModelSerializer):

    grade = GradeModelSerializer()

    class Meta:

        model = StudentModel
        fields = "__all__"