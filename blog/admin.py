'''
File hosting the admin section code
'''

from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Decorator to register both Post-class & PostAdmin-class into admin site
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    # Field we want to use Summernote for
    summernote_fields = ('content',)
    # Field we want slug prepopulated for
    prepopulated_fields = {'slug': ('title',)}
    # Fields each post is searchable for
    search_fields = ['title', 'content', 'created_on']
    # Fields each post can be filtered for
    list_filter = ('status', 'created_on', 'updated_on')
    # Fields each post can be managed for
    list_display = ('title', 'slug', 'status', 'created_on', 'author')


# Decorator to register both Comment-class & CommentAdmin-class into admin site
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    # Fields each comment is searchable for
    search_fields = ('commentator', 'email', 'body')
    # Fields each comment can be filtered for
    list_filter = ('created_on', 'updated_on')
    # Fields each comment can be managed for
    list_display = ('commentator', 'body', 'post', 'created_on', 'updated_on')
