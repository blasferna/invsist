# Generated by Django 3.1 on 2021-12-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20211204_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
