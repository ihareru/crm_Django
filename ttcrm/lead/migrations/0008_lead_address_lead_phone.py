# Generated by Django 4.1 on 2024-03-26 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0007_leadfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
