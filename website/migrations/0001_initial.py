# Generated by Django 5.0.2 on 2024-06-20 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=100)),
                ('subdomain', models.CharField(max_length=100)),
                ('video', models.CharField(max_length=1000)),
            ],
        ),
    ]
