# Generated by Django 2.0.1 on 2018-01-19 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='type_of_book',
            field=models.CharField(blank='true', max_length=150, null='False'),
        ),
    ]