# Generated by Django 2.2.5 on 2019-10-20 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191020_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='avater',
            new_name='avatar',
        ),
    ]
