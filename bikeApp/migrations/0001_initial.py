# Generated by Django 3.2.1 on 2021-06-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motobike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.IntegerField()),
                ('bike_model', models.CharField(max_length=200)),
                ('warranty', models.IntegerField()),
                ('bike_owner', models.CharField(max_length=100)),
            ],
        ),
    ]
