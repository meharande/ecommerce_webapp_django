# Generated by Django 3.2.8 on 2021-11-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211102_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='optiongroup',
            name='option',
        ),
        migrations.AddField(
            model_name='optiongroup',
            name='option',
            field=models.ManyToManyField(to='products.Option'),
        ),
    ]
