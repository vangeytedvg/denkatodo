# Generated by Django 3.0.5 on 2020-04-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20200430_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitors',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
