# Generated by Django 4.1 on 2024-03-21 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_client_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('name',)},
        ),
    ]
