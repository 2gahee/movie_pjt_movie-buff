# Generated by Django 4.2.16 on 2024-11-20 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_rename_user_id_article_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article_id',
            new_name='article',
        ),
    ]
