# Generated by Django 2.0.1 on 2018-01-19 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20180119_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_publish',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='number_of_page',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='type_of_book',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
