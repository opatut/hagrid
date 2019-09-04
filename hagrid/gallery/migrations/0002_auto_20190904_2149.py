# Generated by Django 2.2.4 on 2019-09-04 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='caption',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(upload_to='galleryimages/'),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='variation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Variation'),
        ),
    ]
