# Generated by Django 4.2.2 on 2023-06-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_codregistro_user_codigoregistro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]