# Generated by Django 2.2.6 on 2019-10-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0005_auto_20191016_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='categories',
            field=models.ManyToManyField(null=True, to='donation.Category'),
        ),
    ]
