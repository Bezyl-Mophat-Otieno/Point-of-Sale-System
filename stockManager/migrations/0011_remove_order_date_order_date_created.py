# Generated by Django 4.1.7 on 2023-03-30 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockManager', '0010_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.AddField(
            model_name='order',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
