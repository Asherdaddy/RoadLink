# Generated by Django 2.0.4 on 2018-04-12 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_book_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
