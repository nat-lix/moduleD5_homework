# Generated by Django 4.2.5 on 2023-09-12 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_rating_comment_commentrating_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='dateCreatiion',
            new_name='dateCreation',
        ),
    ]