# Generated by Django 2.1.2 on 2018-11-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slambook', '0003_auto_20181104_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fdetail',
            name='pic',
            field=models.ImageField(blank=True, default='1.jpg', upload_to=''),
        ),
    ]