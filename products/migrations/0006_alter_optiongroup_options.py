# Generated by Django 3.2.8 on 2021-11-02 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20211103_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optiongroup',
            name='options',
            field=models.ManyToManyField(related_name='options_groups', to='products.Option', verbose_name='options_groups'),
        ),
    ]
