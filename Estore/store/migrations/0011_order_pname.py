# Generated by Django 3.0.7 on 2020-11-25 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pname',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
