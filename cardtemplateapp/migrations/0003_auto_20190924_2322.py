# Generated by Django 2.2.5 on 2019-09-25 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardtemplateapp', '0002_auto_20190921_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothing',
            name='clothing_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='personality',
            name='personality_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]