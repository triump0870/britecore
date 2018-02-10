# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from app.models import *
from apis.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# Create your views here.
class RiskFieldListCreateAPI(ListCreateAPIView):
    queryset = RiskField.objects.all()
    serializer_class = RiskFieldSerializer


class RiskTypeListCreateAPI(ListCreateAPIView):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer


class RiskListCreateAPI(ListCreateAPIView):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'riskfields': reverse('api:risk_fields', request=request, format=format),
        'risktypes': reverse('api:risk_types', request=request, format=format),
        'risks': reverse('api:risks', request=request, format=format),
    })
