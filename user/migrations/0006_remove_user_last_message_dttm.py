# Generated by Django 4.2.4 on 2023-08-08 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_last_message_dttm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_message_dttm',
        ),
    ]