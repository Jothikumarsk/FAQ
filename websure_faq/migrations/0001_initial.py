# Generated by Django 3.0.3 on 2020-08-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('question_text', models.CharField(max_length=300)),
                ('url', models.URLField()),
                ('publish_date', models.DateTimeField(verbose_name='date published')),
                ('answer', models.CharField(max_length=1000, default='')),
            ],
        ),
    ]
