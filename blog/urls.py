from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^category/(?P<category_id>\d+)$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_id>\d+)$', views.TagView.as_view(), name='tag'),
    url(r'^search/$', views.SearchView.as_view(), name='search'),
    url(r'^link/$', views.LinkView.as_view(),  name='link')
]