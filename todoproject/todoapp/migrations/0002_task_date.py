# Generated by Django 4.2 on 2023-05-08 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-11-25'),
            preserve_default=False,
        ),
    ]