# Generated by Django 3.0.7 on 2020-11-25 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20201125_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
