# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('body', models.TextField(verbose_name='正文')),
                ('description', models.CharField(blank=True, null=True, max_length=140, help_text='可选，为空则自动选取前140个字符', verbose_name='摘要')),
                ('status', models.CharField(max_length=1, choices=[('p', '发布'), ('t', '草稿'), ('d', '删除')], verbose_name='状态', default='p')),
                ('time_create', models.DateTimeField(verbose_name='发布时间', default=django.utils.timezone.now)),
                ('time_last_modified', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('views', models.PositiveIntegerField(verbose_name='浏览量', default=0)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'ordering': ['-time_create'],
                'verbose_name_plural': '文章数据',
                'verbose_name': '文章数据',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='标题')),
                ('order', models.IntegerField(verbose_name='排序', default=0)),
                ('description', models.CharField(blank=True, max_length=140, null=True, verbose_name='摘要', default='一个分类')),
                ('img', models.CharField(max_length=240, verbose_name='图片地址', default='/static/category/django.png')),
                ('time_create', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-time_create'],
                'verbose_name_plural': '分类数据',
                'verbose_name': '分类数据',
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='标题')),
                ('url', models.CharField(max_length=240, verbose_name='URL地址')),
                ('order', models.IntegerField(verbose_name='排序', default=0)),
                ('time_create', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
                ('is_show', models.BooleanField(help_text='选择是否在菜单显示，默认显示', verbose_name='显示', default=True)),
            ],
            options={
                'ordering': ['-time_create'],
                'verbose_name_plural': '导航数据',
                'verbose_name': '导航数据',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='标题')),
                ('order', models.IntegerField(verbose_name='排序', default=0)),
                ('time_create', models.DateTimeField(verbose_name='创建时间', default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-time_create'],
                'verbose_name_plural': '标签数据',
                'verbose_name': '标签数据',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, verbose_name='分类', to='blog.Category', on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', blank=True, verbose_name='标签'),
        ),
    ]
