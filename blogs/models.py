from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length = 50, unique = True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

# in the search field in admin panel when we search for Draft or Published than it will search for that section, earlier we wrote 0 and 1 which is not the correct way, because we user searches on basis of status than if he search with draft or published key-word than nothing will be displayed because we colud have used 0 and 1 in our code...best practice is to write whatever you want the user will be searching in correct way for status

STATUS_CHOICES = (
    # (0, "Draft"),
    ("Draft", "Draft"),
    # (1, "Published")
    ("Published", "Published")
)
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #using cascade because when you delete specific category the blog post associated should also be deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE) # so when user is deleted hte blog post of that user should also be deleted
    featured_image = models.ImageField(upload_to='uploads/%d/%m/%Y')
    short_description= models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title