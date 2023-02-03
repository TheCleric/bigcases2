# Generated by Django 4.1.5 on 2023-01-27 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        help_text="The moment when the item was created.",
                    ),
                ),
                (
                    "date_modified",
                    models.DateTimeField(
                        auto_now=True,
                        db_index=True,
                        help_text="The last moment when the item was modified. A value in year 1750 indicates the value is unknown",
                    ),
                ),
                (
                    "docket_name",
                    models.TextField(help_text="The name of the docket"),
                ),
                (
                    "docket_number",
                    models.CharField(
                        blank=True,
                        help_text="The docket numbers of a case",
                        max_length=100,
                    ),
                ),
                (
                    "court_name",
                    models.CharField(
                        help_text="The court where the upload was from",
                        max_length=100,
                    ),
                ),
                (
                    "case_summary",
                    models.CharField(
                        blank=True,
                        help_text="A few words to describe the case in social media",
                        max_length=100,
                    ),
                ),
                (
                    "cl_docket_id",
                    models.IntegerField(
                        help_text="The docket id from CourtListener db.",
                        null=True,
                    ),
                ),
                (
                    "cl_court_id",
                    models.CharField(
                        help_text="The CL court ID, b/c it's sometimes different from PACER's",
                        max_length=100,
                    ),
                ),
                (
                    "pacer_court_id",
                    models.CharField(
                        help_text="The ID in PACER's subdomain", max_length=10
                    ),
                ),
                (
                    "pacer_case_id",
                    models.CharField(
                        blank=True,
                        help_text="The cased ID provided by PACER. Noted in this case on a per-document-level, since we've learned that some documents from other cases can appear in curious places.",
                        max_length=100,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]