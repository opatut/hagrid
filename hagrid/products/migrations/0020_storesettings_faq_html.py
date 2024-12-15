# Generated by Django 4.2.16 on 2024-12-15 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0019_variation_count_disabled_reason_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="storesettings",
            name="faq_html",
            field=models.TextField(
                blank=True,
                default="",
                help_text="HTML that will be rendered on the FAQ page",
            ),
        ),
    ]
