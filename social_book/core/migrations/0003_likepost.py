# Generated by Django 3.2.4 on 2023-08-10 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
