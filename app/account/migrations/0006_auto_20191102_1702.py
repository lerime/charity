# Generated by Django 2.2.5 on 2019-11-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20191030_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='group_size',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
