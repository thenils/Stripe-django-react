# Generated by Django 3.2 on 2021-10-10 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_subscription_feature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='feature',
        ),
    ]
