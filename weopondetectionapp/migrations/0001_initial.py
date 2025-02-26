# Generated by Django 5.1.4 on 2024-12-19 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='weopons/')),
            ],
        ),
        migrations.CreateModel(
            name='LoginTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('password', models.CharField(blank=True, max_length=30, null=True)),
                ('usertype', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('phonenumber', models.BigIntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weopondetectionapp.logintable')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(blank=True, max_length=300, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weopondetectionapp.usertable')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(blank=True, max_length=300, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('reply', models.CharField(blank=True, max_length=300, null=True)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weopondetectionapp.usertable')),
            ],
        ),
    ]
