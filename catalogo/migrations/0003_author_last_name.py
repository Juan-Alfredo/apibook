# Generated by Django 3.2.3 on 2021-06-05 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20210603_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
