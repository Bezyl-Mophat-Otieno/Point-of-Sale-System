# Generated by Django 4.1.7 on 2023-03-30 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockManager', '0011_remove_order_date_order_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
