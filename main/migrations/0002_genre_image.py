# Generated by Django 3.1 on 2021-09-02 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='genres'),
        ),
    ]
