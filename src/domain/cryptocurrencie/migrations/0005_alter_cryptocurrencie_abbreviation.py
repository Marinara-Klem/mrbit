# Generated by Django 3.2.4 on 2021-06-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocurrencie', '0004_alter_wallet_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrencie',
            name='abbreviation',
            field=models.CharField(max_length=10),
        ),
    ]
