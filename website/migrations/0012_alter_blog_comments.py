# Generated by Django 4.2.4 on 2023-08-31 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_blog_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, related_name='blogs', to='website.comment'),
        ),
    ]