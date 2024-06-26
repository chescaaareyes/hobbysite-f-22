# Generated by Django 5.0.4 on 2024-05-05 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0003_threadcategory_thread_comment_delete_post_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="thread",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="thread",
                to="forum.thread",
            ),
        ),
        migrations.AlterField(
            model_name="thread",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="category",
                to="forum.threadcategory",
            ),
        ),
    ]
