# Generated by Django 4.2.13 on 2024-06-18 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_friendrequest_status'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='user1',
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='user2',
        ),
        migrations.RemoveField(
            model_name='friendrequest',
            name='accepted',
        ),
        migrations.DeleteModel(
            name='FriendRequestRateLimit',
        ),
        migrations.DeleteModel(
            name='Friendship',
        ),
    ]