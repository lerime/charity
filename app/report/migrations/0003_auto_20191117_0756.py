# Generated by Django 2.2.5 on 2019-11-17 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20191027_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='epistle',
            field=models.PositiveIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='report',
            name='evenint_super_pray',
            field=models.PositiveIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='report',
            name='fasting',
            field=models.PositiveIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='report',
            name='jawshan',
            field=models.PositiveIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='report',
            name='night_pray',
            field=models.PositiveIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='report',
            name='pray',
            field=models.PositiveIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='report',
            name='quran',
            field=models.PositiveIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='report',
            name='super_pray',
            field=models.PositiveIntegerField(default=-1),
        ),
    ]
