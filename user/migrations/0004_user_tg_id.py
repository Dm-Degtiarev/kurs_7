# Generated by Django 4.2.4 on 2023-08-08 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_tg_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tg_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID пользователя в телеграм'),
        ),
    ]
