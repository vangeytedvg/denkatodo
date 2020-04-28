from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

STATUS = (
    (0, 'DRAFT'),
    (1, 'PUBLISHED'),
    (2, 'BLAMED')
)


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(default='', editable=False, max_length=200, unique=True, null=True)
    content = models.TextField(null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateField(auto_now_add=True, null=True)
    date_update = models.DateField(auto_now=True, null=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete= models.CASCADE,related_name='blog_posts', default=1)

    class Meta:
        ordering = ['date_created']
        
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)