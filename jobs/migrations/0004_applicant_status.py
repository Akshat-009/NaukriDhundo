# Generated by Django 3.1.7 on 2021-03-15 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20210315_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
