# Generated by Django 3.1.7 on 2021-03-26 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall_messages_app', '0003_auto_20210325_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_comment', to='wall_messages_app.messages'),
        ),
    ]