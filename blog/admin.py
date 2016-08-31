from django.contrib import admin, messages
from blog.models import Article, Category, Tag, MyUser, Nav
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'category', 'time_last_modified', 'views', 'status_ico')

    actions = ('make_publish', 'make_temp', 'make_delete')

    def make_publish(self, request, queryset):
        num = queryset.update(status='p')
        message = "%s 篇文章已经标记为发布状态" % num
        messages.success(request, message=message)
    make_publish.short_description = '将文章设置为发布状态'

    def make_temp(self, request, queryset):
        num = queryset.update(status='t')
        message = "%s 篇文章已经标记为草稿状态" % num
        messages.success(request, message=message)
    make_temp.short_description = '将文章设置为草稿状态'

    def make_delete(self, request, queryset):
        num = queryset.update(status='d')
        message = "%s 篇文章已经标记为删除状态" % num
        messages.success(request, message=message)
    make_delete.short_description = '将文章设置为删除状态'

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'body',)
        }),
        ('更多', {
            'fields': ('category', 'tag'),
        }),
        ('其他', {
            'fields': ('status', 'time_create', 'views'),
            'classes': ['collapse'],
        }),
    )

    class Media:
        js = ['blog/js/tinymce/tinymce.min.js', 'blog/js/tinymce/textareas.js']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'description', 'time_create', 'img_ico')

    fieldsets = (
        ('基本设置', {
            'fields': ('title', 'description', 'order', 'img')
        }),
    )


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

    fieldsets = (
        ('基本设置', {
            'fields': ('title', 'order')
        }),
    )


class NavAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'url', 'is_show')

    fieldsets = (
        ('基本设置', {
            'fields': ('title', 'order', 'url', 'is_show')
        }),
    )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Nav, NavAdmin)
admin.site.register(MyUser)
