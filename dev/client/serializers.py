from rest_framework import serializers

from .models import Client, HealthProblem


class HealthProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model=HealthProblem
        fields=['name', 'grade']

class ClientSerializer(serializers.ModelSerializer):
    health_problem = HealthProblemSerializer(many=True)

    class Meta:
        model=Client
        fields=['name', 'birth_date', 'gender', 'health_problem', 'created_at', 'att_at']

    def create(self, validated_data):
        problems_data = validated_data.pop('health_problem')
        client = Client.objects.create(**validated_data)
        for problem in problems_data:
            HealthProblem.objects.create(**problem)
        return client