# Generated by Django 5.0.4 on 2024-04-14 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='us_last_name',
            name='id',
        ),
        migrations.AlterField(
            model_name='us_last_name',
            name='name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
