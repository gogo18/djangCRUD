# Generated by Django 2.0.1 on 2018-01-19 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_auto_20180119_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_publish',
            field=models.DateField(blank=True, null=True),
        ),
    ]
