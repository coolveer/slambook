# Generated by Django 2.1.2 on 2018-11-03 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slambook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fdetail',
            name='fkey',
            field=models.CharField(max_length=9999),
        ),
    ]
