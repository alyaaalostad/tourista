# Generated by Django 2.0.7 on 2019-08-26 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]