# Generated by Django 3.1.5 on 2021-09-20 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='exam',
            field=models.CharField(max_length=50),
        ),
    ]
