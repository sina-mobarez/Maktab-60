# Generated by Django 3.2.9 on 2021-12-08 16:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_alter_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='blog_comments', to=settings.AUTH_USER_MODEL, verbose_name='likes on post'),
        ),
    ]