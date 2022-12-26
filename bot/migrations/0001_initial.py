# Generated by Django 4.1.4 on 2022-12-25 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(null=True)),
                ('language', models.CharField(max_length=256, null=True)),
                ('state', models.IntegerField(null=True)),
                ('invited_by', models.BigIntegerField(null=True)),
            ],
        ),
    ]
