from django.shortcuts import render
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Article, Category, Tag
from django.conf import settings

# Create your views here.


# 首页视图
class IndexView(ListView):
    template_name = 'blog/list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        articles = Article.objects.filter(status='p')
        return articles

    def get_context_data(self, **kwargs):
        kwargs['title'] = '首页'
        return super(IndexView, self).get_context_data(**kwargs)


# 分类视图
class CategoryView(ListView):
    template_name = 'blog/list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        category_id = int(self.kwargs['category_id'])
        if category_id == 0:
            articles = Article.objects.filter(category__isnull=True, status='p')
        else:
            articles = Article.objects.filter(category=category_id, status='p')
        return articles

    def get_context_data(self, **kwargs):
        try:
            kwargs['title'] = '分类:' + Category.objects.filter(pk=self.kwargs['category_id'])[0].title
        except IndexError:
            kwargs['title'] = '没有找到这个分类!'
        return super(CategoryView, self).get_context_data(**kwargs)


# 标签视图
class TagView(ListView):
    template_name = 'blog/list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        articles = Article.objects.filter(tag=self.kwargs['tag_id'], status='p')
        return articles

    def get_context_data(self, **kwargs):
        try:
            kwargs['title'] = '标签:' + Tag.objects.filter(pk=self.kwargs['tag_id'])[0].title
        except IndexError:
            kwargs['title'] = '没有找到标签!'
        return super(TagView, self).get_context_data(**kwargs)


# 搜索视图
class SearchView(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'articles'

    def get_queryset(self):
        query = self.request.GET['query']
        articles = Article.objects.filter(status='p').filter(Q(body__contains=query) |
                                          Q(title__contains=query) |
                                          Q(description__contains=query))
        return articles

    def get_context_data(self, **kwargs):
        kwargs['title'] = '搜索:' + self.request.GET['query']
        kwargs['query'] = self.request.GET['query']
        return super(SearchView, self).get_context_data(**kwargs)


# 文章详情视图
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

    def get_object(self):
        obj = super(ArticleDetailView, self).get_object()
        if obj.status == 'p':
            obj.viewed()
            return obj

    def get_context_data(self, **kwargs):
        kwargs['title'] = super(ArticleDetailView, self).get_object().title
        return super(ArticleDetailView, self).get_context_data(**kwargs)
