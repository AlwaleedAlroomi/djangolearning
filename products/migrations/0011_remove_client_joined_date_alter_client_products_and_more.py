# Generated by Django 4.2.5 on 2023-09-21 16:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_client_joined_date_alter_product_added_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='joined_date',
        ),
        migrations.AlterField(
            model_name='client',
            name='Products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='added_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 21, 16, 46, 54, 637752, tzinfo=datetime.timezone.utc), verbose_name='Added Date'),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('joined_date', models.DateField(default=datetime.datetime(2023, 9, 21, 16, 46, 54, 637752, tzinfo=datetime.timezone.utc), verbose_name='Joined Date')),
                ('Products', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
