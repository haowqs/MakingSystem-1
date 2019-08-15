<<<<<<< HEAD
# Generated by Django 2.2.4 on 2019-08-12 12:22
=======
# Generated by Django 2.2.4 on 2019-08-11 13:29
>>>>>>> b48fcee63e8af073648b37a9415508d1921e024a

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
<<<<<<< HEAD
                ('real_name', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=11)),
                ('gender', models.BooleanField(default=False)),
                ('email', models.EmailField(blank=True, max_length=20, null=True)),
                ('school', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=10)),
                ('profession', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('date_birth', models.DateField(auto_now_add=True)),
                ('grade', models.CharField(max_length=10)),
                ('education', models.CharField(max_length=10)),
                ('vocation', models.CharField(max_length=20)),
=======
                ('real_name', models.CharField(max_length=10, null=True)),
                ('mobile', models.CharField(max_length=11)),
                ('gender', models.BooleanField(default=False)),
                ('email', models.EmailField(blank=True, max_length=20, null=True)),
                ('school', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=10)),
                ('profession', models.CharField(max_length=20, null=True)),
                ('number', models.IntegerField(null=True)),
                ('date_birth', models.DateField(auto_now_add=True)),
                ('grade', models.CharField(max_length=10, null=True)),
                ('education', models.CharField(max_length=10, null=True)),
                ('vocation', models.CharField(max_length=20, null=True)),
>>>>>>> b48fcee63e8af073648b37a9415508d1921e024a
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
