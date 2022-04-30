from apps.recommender.models import Motorcycle
from rest_framework import serializers


class MotorcycleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Motorcycle
        fields = ['name', 'brand_id', 'year', 'price']