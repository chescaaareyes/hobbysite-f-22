# Generated by Django 5.0.4 on 2024-05-08 15:01

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("commissions", "0011_alter_commission_author"),
        ("user_management", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobapplication",
            name="applicant",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="job_application",
                to="user_management.profile",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="job",
            field=models.ForeignKey(
                editable=False,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="job_application",
                to="commissions.job",
            ),
        ),
    ]
