# Generated by Django 5.1 on 2024-08-28 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('father_name', models.CharField(max_length=30)),
                ('address', models.TextField()),
            ],
        ),
    ]