# Generated by Django 3.0.3 on 2020-08-20 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websure_faq', '0002_auto_20200819_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='link',
            field=models.FilePathField(allow_folders=True, blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='question',
            name='url',
            field=models.URLField(blank=True, default=None),
        ),
    ]
