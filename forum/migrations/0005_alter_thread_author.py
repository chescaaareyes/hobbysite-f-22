# Generated by Django 5.0.4 on 2024-05-06 06:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0004_alter_comment_thread_alter_thread_category"),
        ("user_management", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="thread",
            name="author",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="thread_author",
                to="user_management.profile",
            ),
        ),
    ]
