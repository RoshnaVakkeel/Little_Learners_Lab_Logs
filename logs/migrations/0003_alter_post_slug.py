# Generated by Django 3.2.16 on 2023-01-10 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
