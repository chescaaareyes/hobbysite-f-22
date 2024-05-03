# Generated by Django 5.0.2 on 2024-05-03 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0004_alter_commission_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Full', 'Full'), ('Completed', 'Completed'), ('Discontinued', 'Discontinued')], default='Open', max_length=12),
        ),
    ]
