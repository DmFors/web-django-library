# Generated by Django 4.1.1 on 2022-09-19 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publish_date',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
    ]
