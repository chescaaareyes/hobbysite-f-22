# Generated by Django 5.0.4 on 2024-05-08 15:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_article_headerimage_alter_comment_createdon"),
        ("user_management", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="articles",
                to="user_management.profile",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="comments",
                to="user_management.profile",
            ),
        ),
    ]