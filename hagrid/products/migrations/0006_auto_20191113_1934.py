# Generated by Django 2.2.4 on 2019-11-13 18:34

from django.db import migrations
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20191113_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizegroup',
            name='position',
            field=positions.fields.PositionField(default=None, null=True),
        ),
    ]
