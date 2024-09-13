"""Serializers."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the Task model."""

    class Meta:
        """Meta class."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
