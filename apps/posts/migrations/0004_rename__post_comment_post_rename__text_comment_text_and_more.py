# Generated by Django 5.1.4 on 2024-12-28 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_remove_post_comments_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="_post",
            new_name="post",
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="_text",
            new_name="text",
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="_user",
            new_name="user",
        ),
    ]
