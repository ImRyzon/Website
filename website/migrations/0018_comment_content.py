# Generated by Django 4.2.4 on 2023-09-03 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_alter_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default=None, max_length=1024),
        ),
    ]