# Generated by Django 2.2.5 on 2019-10-27 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20191027_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='course',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Course'),
        ),
    ]
