# Generated by Django 4.2.4 on 2023-08-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_tg_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_message_dttm',
            field=models.TimeField(blank=True, null=True, verbose_name='Время последней отправки'),
        ),
    ]
