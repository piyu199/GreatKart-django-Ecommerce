# Generated by Django 3.1 on 2023-05-04 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=1000, unique=True),
        ),
    ]
