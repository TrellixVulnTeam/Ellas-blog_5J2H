# Generated by Django 3.1.2 on 2020-11-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20201111_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
