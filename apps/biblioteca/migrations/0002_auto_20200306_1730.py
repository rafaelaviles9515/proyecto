# Generated by Django 2.2.4 on 2020-03-07 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]