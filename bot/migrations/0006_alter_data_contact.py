# Generated by Django 4.1.6 on 2023-10-06 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_data_invited_people_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='contact',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
