from rest_framework import serializers

from .models import ColocacionVacuna


class VacunacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColocacionVacuna
        fields = '__all__'