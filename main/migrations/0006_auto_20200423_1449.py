# Generated by Django 3.0.5 on 2020-04-23 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_todo_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
