# Generated by Django 3.0.3 on 2020-05-08 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManagementTool', '0006_auto_20200508_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='quantity',
            field=models.IntegerField(default=0, max_length=6),
        ),
    ]