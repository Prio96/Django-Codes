# Generated by Django 5.1 on 2024-09-14 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_author_bio'),
        ('posts', '0003_alter_post_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]