# Generated by Django 2.2.5 on 2019-10-26 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=500, null=True)),
                ('optionA', models.CharField(blank=True, max_length=255, null=True)),
                ('optionB', models.CharField(blank=True, max_length=255, null=True)),
                ('optionC', models.CharField(blank=True, max_length=255, null=True)),
                ('optionD', models.CharField(blank=True, max_length=255, null=True)),
                ('answer', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]