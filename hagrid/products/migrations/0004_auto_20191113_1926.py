# Generated by Django 2.2.4 on 2019-11-13 18:26

from django.db import migrations
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_storesettings_dashboard_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['position']},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'ordering': ['position']},
        ),
        migrations.AlterModelOptions(
            name='sizegroup',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='product',
            name='position',
            field=positions.fields.PositionField(default=-1),
        ),
        migrations.AddField(
            model_name='size',
            name='position',
            field=positions.fields.PositionField(default=-1),
        ),
        migrations.AddField(
            model_name='sizegroup',
            name='position',
            field=positions.fields.PositionField(default=-1),
        ),
    ]
