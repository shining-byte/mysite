# Generated by Django 2.1.4 on 2018-12-23 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181223_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homebanner',
            name='author',
            field=models.CharField(max_length=30, verbose_name='作者'),
        ),
    ]