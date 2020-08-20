# Generated by Django 3.0.5 on 2020-08-18 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmpages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorform',
            name='Phone',
        ),
        migrations.RemoveField(
            model_name='vendorform',
            name='passwoed2',
        ),
        migrations.AddField(
            model_name='vendorform',
            name='password2',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='vendorform',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='vendorform',
            name='city',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='vendorform',
            name='country',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='vendorform',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='vendorform',
            name='password1',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='vendorform',
            name='pincode',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='vendorform',
            name='state',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='vendorform',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]