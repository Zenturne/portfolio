# Generated by Django 2.2.6 on 2019-10-16 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0003_auto_20191016_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='type',
            field=models.IntegerField(choices=[(1, 'fundacja'), (2, 'organizacja pozarządowa'), (3, 'zbiórka lokalna')], max_length=24),
        ),
    ]
