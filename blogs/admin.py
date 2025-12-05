from django.contrib import admin
from .models import Category, Blog, Comment

# (Pre-Populated Slug:) this is supposed to be done whenever you create a slug, now slug means that for example https:chrome/blogs/this-is-sports-news...so after blog/ whatever text is written is supposed to be the slug for what blog-post you are viewing, in admin page using this function ifincase the title of blog is very large than we can't time the slug manually so this function basically automatically fills up the slug on bassis of what title the user is giving to create the blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured', ) 
    # if you want to make any data-model in admin to be editable

# we wrote cateogry__category_name because we wnat to search with the name of the category because as we have mentioned in the models.py in Category function than we wnat to display category_name so thats y we wrote that...

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
