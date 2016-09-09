from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone
from django.conf import settings
# Create your models here.


# 文章模型
class Article(models.Model):
    STATUS_CHOICES = (
        ('p', '发布'),
        ('t', '草稿'),
        ('d', '删除'),
    )
    title = models.CharField('标题', max_length=100)
    body = models.TextField('正文')
    description = models.CharField('摘要', max_length=140, blank=True, null=True,
                                   help_text='可选，为空则自动选取前140个字符')
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag', verbose_name='标签', blank=True)
    category = models.ForeignKey('Category', verbose_name='分类', blank=True, null=True, on_delete=models.SET_NULL)
    status = models.CharField('状态', max_length=1, choices=STATUS_CHOICES, default='p')
    time_create = models.DateTimeField('发布时间', default=timezone.now)
    time_last_modified = models.DateTimeField('修改时间', auto_now=True)
    views = models.PositiveIntegerField('浏览量', default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        verbose_name = '文章数据'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        """获取文章地址"""
        return reverse('blog:detail', kwargs={'article_id': self.pk})

    def status_ico(self):
        """后台发布状态的图标"""
        img = 'sign-check.png'
        if self.status == 'd':
            img = 'sign-error.png'
        elif self.status == 't':
            img = 'sign-warning.png'
        return '<img src="/static/images/%s">' % img
    status_ico.allow_tags = True
    status_ico.admin_order_field = 'status'
    status_ico.short_description = "状态"

    def save(self,  *args, **kwargs):
        """文章描述的截取"""
        self.description = self.description or self.body[:140]
        super().save(*args, **kwargs)

    def viewed(self):
        """浏览量加1"""
        self.views += 1
        self.save(update_fields=['views'])

    def get_previous_article(self):
        """获取上一篇文章"""
        all_item = Article.objects.filter(status='p').order_by('id')
        index = 0
        for x in all_item:
            if x.id == self.id:
                break
            else:
                index += 1
        if index:
            return all_item[index-1]

    def get_next_article(self):
        """获取下一篇文章"""
        all_item = Article.objects.filter(status='p').order_by('-id')
        index = 0
        for x in all_item:
            if x.id == self.id:
                break
            else:
                index += 1
        if index:
            return all_item[index-1]


# 分类模型
class Category(models.Model):
    title = models.CharField('标题', max_length=40)
    order = models.IntegerField('排序', default=0)
    description = models.CharField('摘要', max_length=140, blank=True, null=True, default='一个分类')
    img = models.CharField('图片地址', default='/static/category/django.png', max_length=240)
    time_create = models.DateTimeField('创建时间', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        verbose_name = '分类数据'
        verbose_name_plural = verbose_name

    def img_ico(self):
        """分类图片"""
        return '<img src="%s" height="40px" width="100">' % self.img
    img_ico.allow_tags = True
    img_ico.admin_order_field = 'img'
    img_ico.short_description = "图片"

    def p_count(self):
        """分类下发布状态的文章数量"""
        count = self.article_set.filter(status='p').count()
        return count


# 标签模型
class Tag(models.Model):
    title = models.CharField('标题', max_length=40)
    order = models.IntegerField('排序', default=0)
    time_create = models.DateTimeField('创建时间', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        verbose_name = '标签数据'
        verbose_name_plural = verbose_name


# 导航模型
class Nav(models.Model):
    title = models.CharField('标题', max_length=40)
    url = models.CharField('URL地址', max_length=240)
    order = models.IntegerField('排序', default=0)
    time_create = models.DateTimeField('创建时间', default=timezone.now)
    is_show = models.BooleanField('显示', default=True, help_text='选择是否在菜单显示，默认显示')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        verbose_name = '导航数据'
        verbose_name_plural = verbose_name


class Link(models.Model):
    title = models.CharField('网站标题', max_length=100)
    url = models.URLField('网站链接', default='http://')
    description = models.CharField('网站描述', max_length=240, help_text='网站描述，240字以内', blank=True)
    order = models.PositiveIntegerField('排序', default=0)
    time_create = models.DateTimeField('创建时间', default=timezone.now)
    views = models.PositiveIntegerField('访问次数', default=0)
    is_show = models.BooleanField('显示', default=True, help_text='选择是否在菜单显示，默认显示')

    def __str__(self):
        return self.title

    def viewed(self):
        """浏览量加1"""
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        ordering = ['-time_create']
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

