# Generated by Django 5.0.2 on 2024-03-19 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article_category', to='wiki.articlecategory'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
