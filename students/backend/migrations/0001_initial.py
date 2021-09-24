# Generated by Django 3.1.5 on 2021-09-20 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollno', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('exam', models.CharField(max_length=10)),
                ('marks', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]