# Generated by Django 4.2.4 on 2023-08-31 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_remove_comment_depth'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]