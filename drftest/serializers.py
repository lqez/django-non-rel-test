from rest_framework import serializers
from models import OtherInfo, ModelInfo


class other_info_serializer(serializers.ModelSerializer):
    class Meta:
        model = OtherInfo
        fields = ('info_1', 'info_2', 'info_3')


class mySerializer(serializers.ModelSerializer):
    other_info = other_info_serializer(many=True)

    class Meta:
        model = ModelInfo
        fields = ('name', 'email', 'other_info')
