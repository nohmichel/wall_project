# Generated by Django 3.1.7 on 2021-03-26 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall_messages_app', '0002_auto_20210325_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
