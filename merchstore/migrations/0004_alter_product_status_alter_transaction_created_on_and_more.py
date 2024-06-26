# Generated by Django 5.0.4 on 2024-05-06 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0003_alter_product_owner_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('On sale', 'On Sale'), ('Out of Stock', 'Out of Stock')], default='Available', max_length=12),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('On Cart', 'On Cart'), ('To Pay', 'To Pay'), ('To Shop', 'To Shop'), ('To Receive', 'To Receive'), ('Delivered', 'Delivered')], max_length=10),
        ),
    ]
