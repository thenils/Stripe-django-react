# Generated by Django 3.2 on 2021-10-10 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('subscription_id', models.CharField(max_length=255)),
                ('feature', models.JSONField(default={'features': []})),
            ],
        ),
    ]
