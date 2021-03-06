# Generated by Django 2.1.2 on 2018-11-01 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, default='1.jpg', upload_to='')),
                ('name', models.CharField(max_length=9999)),
                ('home', models.CharField(max_length=9999)),
                ('pno', models.CharField(max_length=9999)),
                ('born', models.CharField(max_length=9999)),
                ('become', models.CharField(max_length=9999)),
                ('dream', models.CharField(max_length=9999)),
                ('sport', models.CharField(max_length=9999)),
                ('relation', models.CharField(max_length=9999)),
                ('look', models.CharField(max_length=9999)),
                ('eat', models.CharField(max_length=9999)),
                ('movies', models.CharField(max_length=9999)),
                ('dislike', models.CharField(max_length=9999)),
                ('crazy', models.CharField(max_length=9999)),
                ('moment', models.CharField(max_length=9999)),
                ('holiday', models.CharField(max_length=9999)),
                ('friendship', models.CharField(max_length=9999)),
                ('withyou', models.CharField(max_length=9999)),
                ('hobbies', models.CharField(max_length=9999)),
                ('truth', models.CharField(max_length=9999)),
                ('you', models.CharField(max_length=9999)),
                ('love', models.CharField(max_length=9999)),
                ('date', models.CharField(max_length=9999)),
                ('fkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
