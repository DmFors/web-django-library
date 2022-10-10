# Generated by Django 4.1.1 on 2022-10-10 19:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_book_publish_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='book',
            name='cost',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(2022)]),
        ),
    ]
