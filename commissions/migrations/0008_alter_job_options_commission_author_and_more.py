# Generated by Django 5.0.2 on 2024-05-05 05:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0007_alter_commission_status_job_delete_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-status', '-manpower', 'role']},
        ),
        migrations.AddField(
            model_name='commission',
            name='author',
            field=models.CharField(default='Anon', max_length=63),
        ),
        migrations.AlterField(
            model_name='commission',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Full', 'Full'), ('Completed', 'Completed'), ('Discontinued', 'Discontinued')], default='Open', max_length=14),
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Full', 'Full')], default='Open', max_length=6),
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=8)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_application', to='commissions.job')),
            ],
            options={
                'ordering': ['status', '-applied_on'],
            },
        ),
    ]
