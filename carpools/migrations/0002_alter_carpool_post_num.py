# Generated by Django 5.0.6 on 2024-05-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpool',
            name='post_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
