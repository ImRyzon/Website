# Generated by Django 4.2.4 on 2023-08-31 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_comment_is_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]