from rest_framework import serializers
from .models import Habit
from .validators import HabitPleasureValidator, HabitRewardOrRelatedValidator, HabitTimeForExecutionValidator, \
    HabitPeriodicityValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            HabitPleasureValidator(),
            HabitRewardOrRelatedValidator(),
            HabitTimeForExecutionValidator(),
            HabitPeriodicityValidator()
        ]