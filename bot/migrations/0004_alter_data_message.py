# Generated by Django 4.1.4 on 2022-12-25 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_data_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='message',
            field=models.BooleanField(default=False),
        ),
    ]
