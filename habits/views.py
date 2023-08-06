from rest_framework import generics

from .pagination import HabitPagination
from .serializers import HabitSerializer
from .models import Habit


class HabitListView(generics.ListCreateAPIView):
    permission_classes = []
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    queryset = Habit.objects.all()

class HabitDetailView(generics.RetrieveAPIView):
    permission_classes = []
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

class HabitCreateView(generics.CreateAPIView):
    permission_classes = []
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

class HabitDeleteView(generics.DestroyAPIView):
    permission_classes = []
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

class HabitUpdateView(generics.UpdateAPIView):
    permission_classes = []
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
