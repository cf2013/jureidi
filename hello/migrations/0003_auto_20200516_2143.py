# Generated by Django 3.0.6 on 2020-05-16 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20200516_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersbot',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usersbot',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
