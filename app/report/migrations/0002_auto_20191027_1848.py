# Generated by Django 2.2.5 on 2019-10-27 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20191027_1140'),
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='report',
            name='day',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='epistle',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='evenint_super_pray',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='fasting',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Group'),
        ),
        migrations.AddField(
            model_name='report',
            name='jawshan',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='night_pray',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='pray',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='quran',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='student_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='super_pray',
            field=models.PositiveIntegerField(default=0),
        ),
    ]