# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-15 06:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('confession', '0001_initial'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_token', models.CharField(max_length=250)),
                ('vote', models.BooleanField(default=1)),
                ('comment_vote_self', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_vote_self_key', to='comment.Comment')),
            ],
            options={
                'db_table': 'comment_vote',
            },
        ),
        migrations.CreateModel(
            name='ConfessionVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_token', models.CharField(max_length=250)),
                ('vote', models.BooleanField(default=1)),
                ('confession_vote_self', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confession_vote_self_key', to='confession.Confession')),
            ],
            options={
                'db_table': 'confession_vote',
            },
        ),
        migrations.AlterUniqueTogether(
            name='confessionvote',
            unique_together=set([('confession_vote_self', 'vote_token')]),
        ),
        migrations.AlterUniqueTogether(
            name='commentvote',
            unique_together=set([('comment_vote_self', 'vote_token')]),
        ),
    ]
