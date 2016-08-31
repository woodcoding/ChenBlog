# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings
import django.db.models.deletion
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], unique=True, verbose_name='username', help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', error_messages={'unique': 'A user with that username already exists.'})),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('url', models.URLField(default='http://', verbose_name='网址', blank=True)),
                ('groups', models.ManyToManyField(related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', to='auth.Group', related_query_name='user', blank=True)),
                ('user_permissions', models.ManyToManyField(related_name='user_set', help_text='Specific permissions for this user.', verbose_name='user permissions', to='auth.Permission', related_query_name='user', blank=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('body', models.TextField(verbose_name='正文')),
                ('description', models.CharField(max_length=140, null=True, verbose_name='摘要', help_text='可选，为空则自动选取前140个字符', blank=True)),
                ('status', models.CharField(max_length=1, default='p', choices=[('p', '发布'), ('t', '草稿'), ('d', '删除')], verbose_name='状态')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('time_last_modified', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('is_top', models.BooleanField(default=False, verbose_name='置顶')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '文章数据',
                'verbose_name_plural': '文章数据',
                'ordering': ['-time_create'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='标题')),
                ('order', models.IntegerField(default=0, verbose_name='排序')),
                ('description', models.CharField(max_length=140, default='一个分类', null=True, verbose_name='摘要', blank=True)),
                ('img', models.URLField(default='http://', verbose_name='图片地址')),
                ('is_menu', models.BooleanField(default=False, verbose_name='加入菜单')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '分类数据',
                'verbose_name_plural': '分类数据',
                'ordering': ['-time_create'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='标题')),
                ('order', models.IntegerField(default=0, verbose_name='排序')),
                ('is_menu', models.BooleanField(default=False, verbose_name='加入菜单')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '标签数据',
                'verbose_name_plural': '标签数据',
                'ordering': ['-time_create'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name='分类', null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Category', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='标签', blank=True),
        ),
    ]
