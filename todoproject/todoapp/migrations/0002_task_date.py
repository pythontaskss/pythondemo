# Generated by Django 4.2.1 on 2023-06-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1994-01-10'),
            preserve_default=False,
        ),
    ]
