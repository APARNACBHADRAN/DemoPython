# Generated by Django 4.2.2 on 2023-06-30 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1992-09-09'),
            preserve_default=False,
        ),
    ]
