# Generated by Django 4.1.1 on 2022-09-19 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_publish_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publish_date',
            new_name='publish_year',
        ),
    ]
