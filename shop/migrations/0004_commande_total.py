# Generated by Django 4.2.1 on 2023-05-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='total',
            field=models.CharField(default='500', max_length=200),
            preserve_default=False,
        ),
    ]
