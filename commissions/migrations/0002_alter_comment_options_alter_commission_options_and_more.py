# Generated by Django 5.0.2 on 2024-04-28 05:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='commission',
            options={'ordering': ['created_on']},
        ),
        migrations.RemoveField(
            model_name='commission',
            name='desc',
        ),
        migrations.AddField(
            model_name='commission',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='entry',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='commission',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
