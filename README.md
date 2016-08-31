# ChenBlog
ChenBlog

# 开发环境
Python版本：3.5
Django版本：1.8

# 如何使用？
##先安装环境
`pip install -r requirements.txt`
##初始化数据库
`python manage.py makemigrations`
`python manage.py migrate`
##创建管理员用户
`python manage.py createsuperuser`
##启动网站
`python manage.py runserver`

#目前具有的功能：

*文章发布功能(Tinymce编辑器)
*代码高亮（prism）
*文章评论（多说）
*分类功能
*标签功能
*导航条菜单自定义功能

#部分代码实现参考：
http://python.usyiyi.cn/django_182/index.html
https://github.com/djangoStudyTeam/DjangoBlog/tree/blog-tutorial
