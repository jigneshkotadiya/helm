# Generated by Django 3.0.1 on 2020-01-01 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('address_one', models.CharField(blank=True, max_length=100, null=True)),
                ('address_two', models.CharField(blank=True, max_length=100, null=True)),
                ('address_three', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('is_student', models.BooleanField(default=False)),
                ('is_lecturer', models.BooleanField(default=False)),
                ('is_hod', models.BooleanField(default=False)),
                ('is_hoo', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
