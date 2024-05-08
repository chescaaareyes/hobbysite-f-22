# Generated by Django 5.0.4 on 2024-05-06 17:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='headerImage',
            field=models.ImageField(blank=True, null=True, upload_to='header_images/'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='createdOn',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]