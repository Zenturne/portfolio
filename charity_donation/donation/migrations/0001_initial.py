# Generated by Django 2.2.6 on 2019-10-16 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, max_length=400, null=True)),
                ('type', models.CharField(choices=[('fu', 'fundacja'), ('op', 'organizacja pozarządowa'), ('zb', 'zbiórka lokalna')], max_length=24)),
                ('categories', models.ManyToManyField(to='donation.Category')),
            ],
        ),
    ]
