# Generated by Django 3.1.2 on 2020-10-11 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_auto_20201011_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_of_the_day',
            field=models.BooleanField(default=False),
        ),
    ]