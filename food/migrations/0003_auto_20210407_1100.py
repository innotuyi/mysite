# Generated by Django 3.1.7 on 2021-04-07 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.netclipart.com/pp/m/219-2197077_wedding-dinner-icons.png', max_length=1000),
        ),
    ]
