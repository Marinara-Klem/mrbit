# Generated by Django 3.2.4 on 2021-06-05 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocurrencie', '0003_alter_wallet_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='amount',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=25),
        ),
    ]