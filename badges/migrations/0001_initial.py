# Generated by Django 3.2 on 2021-07-08 14:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0019_auto_20210528_1122'),
        ('users', '0022_alter_user_secret_hash'),
        ('comments', '0007_auto_20200822_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('code', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256, null=True)),
                ('image', models.URLField()),
                ('price_days', models.IntegerField(default=10)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'badges',
            },
        ),
        migrations.CreateModel(
            name='UserBadge',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_badges', to='badges.badge')),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_badges', to='comments.comment')),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_badges', to='users.user')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_badges', to='posts.post')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_badges', to='users.user')),
            ],
            options={
                'db_table': 'user_badges',
                'unique_together': {('from_user', 'to_user', 'post_id', 'comment_id')},
            },
        ),
    ]
