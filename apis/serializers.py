import json

from rest_framework.serializers import ModelSerializer
from django.utils.text import slugify
from django.db.models import Q

from app.models import RiskType, RiskField, Risk


class RiskFieldSerializer(ModelSerializer):
    class Meta:
        model = RiskField
        fields = ('name', 'slug', 'type')


class RiskTypeSerializer(ModelSerializer):
    risk_field_list = RiskFieldSerializer(source='risk_fields', many=True)

    class Meta:
        model = RiskType
        fields = ('id', 'description', 'name', 'risk_field_list')

    def create(self, validated_data):
        risk_field_list = validated_data.pop('risk_fields')
        instance = RiskType.objects.create(**validated_data)
        data = []
        for item in risk_field_list:
            name = item.pop('name')
            obj = RiskField.objects.filter(Q(slug=slugify(name)) | Q(name=name)).first()
            if obj is not None:
                data.append(obj.id)
        instance.risk_fields = data
        instance.save()
        return instance

    def update(self, instance, validated_data):
        risk_field_list = validated_data.pop('risk_fields')
        data = []
        for item in risk_field_list:
            name = item.pop('name')
            obj = RiskField.objects.filter(Q(slug=slugify(name)) | Q(name=name)).first()
            if obj is not None:
                data.append(obj.id)
        instance.risk_fields = data
        instance.save()
        return instance


class RiskSerializer(ModelSerializer):
    class Meta:
        model = Risk
        fields = ('id', 'name', 'description', 'risk_type', 'data')

    def validate(self, attrs):
        data = attrs['data']
        if not data:
            data = json.dumps({})
        attrs['data'] = data
        return attrs
