# Generated by Django 3.0.5 on 2020-05-22 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20200522_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakfast',
            name='mrp',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='mrp',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='lunch',
            name='mrp',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='special',
            name='mrp',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
