# Generated by Django 3.0.7 on 2020-11-25 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20201125_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
    ]