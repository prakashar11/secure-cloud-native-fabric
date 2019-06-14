# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-05 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScfUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=128, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(max_length=50, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=128, null=True, verbose_name='Last Name')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is Staff')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of Register')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
                ('username', models.CharField(default='', max_length=128, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'scf_user',
                'proxy': False,
                'verbose_name': 'ScfUser',
            },
        ),
    ]