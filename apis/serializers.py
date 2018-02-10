from rest_framework.serializers import ModelSerializer, RelatedField
from app.models import RiskType, RiskField, Risk
import json


class RiskFieldSerializer(ModelSerializer):
    class Meta:
        model = RiskField
        fields = '__all__'


class RiskTypeSerializer(ModelSerializer):
    risk_field_list = RiskFieldSerializer(source='risk_fields', many=True)

    class Meta:
        model = RiskType
        fields = ('id', 'description', 'risk_field_list')


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
