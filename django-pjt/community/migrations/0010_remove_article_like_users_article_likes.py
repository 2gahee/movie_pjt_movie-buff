# Generated by Django 4.2.16 on 2024-11-25 05:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0009_alter_article_user_alter_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='like_users',
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
