# Generated by Django 4.1.7 on 2023-03-28 07:32

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('stockManager', '0006_alter_order_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='order',
            managers=[
                ('balance', django.db.models.manager.Manager()),
            ],
        ),
    ]
