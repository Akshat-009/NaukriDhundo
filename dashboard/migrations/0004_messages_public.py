# Generated by Django 3.1.7 on 2021-03-17 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]