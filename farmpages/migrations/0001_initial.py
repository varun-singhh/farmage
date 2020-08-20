# Generated by Django 3.0.5 on 2020-08-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VendorForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('Phone', models.IntegerField()),
                ('password1', models.CharField(max_length=32)),
                ('passwoed2', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('pincode', models.IntegerField(max_length=6)),
                ('state', models.CharField(max_length=32)),
                ('country', models.CharField(max_length=32)),
            ],
        ),
    ]
