# Generated by Django 3.2.4 on 2023-08-10 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_likepost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likepost',
            old_name='user_id',
            new_name='post_id',
        ),
    ]
