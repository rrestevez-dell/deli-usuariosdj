# Generated by Django 4.2.2 on 2023-06-25 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_codregistro_user_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='codregistro',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
    ]
