# Generated by Django 4.2.5 on 2023-09-21 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_client_joined_date_alter_client_products_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='added_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 21, 16, 57, 38, 236192, tzinfo=datetime.timezone.utc), verbose_name='Added Date'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='joined_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 21, 16, 57, 38, 247205, tzinfo=datetime.timezone.utc), verbose_name='Joined Date'),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('watch', models.ManyToManyField(to='products.client')),
            ],
        ),
    ]
