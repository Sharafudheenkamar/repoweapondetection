# Generated by Django 5.1.4 on 2025-01-09 06:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weopondetectionapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='USER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weopondetectionapp.logintable'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='USER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weopondetectionapp.logintable'),
        ),
        migrations.AddField(
            model_name='logintable',
            name='email',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='logintable',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='logintable',
            name='phonenumber',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='UserTable',
        ),
    ]
