# Generated by Django 3.0.3 on 2020-09-10 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_auto_20200909_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='birthday',
            field=models.TextField(default=''),
        ),
    ]
