# Generated by Django 2.2.6 on 2019-10-09 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffer',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]
