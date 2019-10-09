# Generated by Django 2.2.6 on 2019-10-09 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=60)),
                ('company_email', models.EmailField(max_length=60)),
                ('job_title', models.CharField(max_length=60)),
                ('job_description', models.TextField(max_length=250)),
                ('salary', models.IntegerField()),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]