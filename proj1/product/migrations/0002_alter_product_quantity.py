# Generated by Django 5.1.4 on 2024-12-31 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
