# Generated by Django 3.1 on 2020-10-02 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0007_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email_address',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile_number',
            field=models.IntegerField(max_length=15),
        ),
    ]
