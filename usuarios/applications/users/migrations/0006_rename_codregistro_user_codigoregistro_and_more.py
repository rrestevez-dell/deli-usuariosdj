# Generated by Django 4.2.2 on 2023-06-25 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_codregistro_user_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='codregistro',
            new_name='codigoregistro',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
    ]
