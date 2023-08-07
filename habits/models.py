from django.db.models import *


NULLABLE = {'null': True, 'blank': True}


class Habit(Model):
    """Модель "Привычка" """
    user = ForeignKey('user.User', on_delete=CASCADE, verbose_name="Пользователь")
    place = CharField(max_length=150, verbose_name="Место")
    time = TimeField(default='00:00:00', verbose_name="Время")
    action = CharField(max_length=100, verbose_name="Действие (привычка)")
    pleasure_flag = BooleanField(default=False, verbose_name="Признак приятной привычки")
    related_habit = ForeignKey('self', on_delete=SET_NULL, verbose_name="Связанная привычка", **NULLABLE)
    periodicity = PositiveIntegerField(default=1, verbose_name="Периодичность (в днях)")
    reward = CharField(max_length=100, verbose_name="Вознаграждение", **NULLABLE)
    time_for_execution = TimeField(default='00:01:00', verbose_name="Время на выполнение")
    publicity_flag = BooleanField(default=False, verbose_name="Признак публичности")

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
