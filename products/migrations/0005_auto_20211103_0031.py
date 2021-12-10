# Generated by Django 3.2.8 on 2021-11-02 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20211103_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='optiongroup',
            name='option',
        ),
        migrations.AddField(
            model_name='optiongroup',
            name='options',
            field=models.ManyToManyField(related_name='options_groups', to='products.Option'),
        ),
        migrations.AlterModelTable(
            name='option',
            table='options',
        ),
        migrations.AlterModelTable(
            name='optiongroup',
            table='option_groups',
        ),
        migrations.AlterModelTable(
            name='optionitem',
            table='option_items',
        ),
    ]