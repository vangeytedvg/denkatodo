# Generated by Django 3.0.5 on 2020-04-24 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_todo_date_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_closed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
