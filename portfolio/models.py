from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, 'DRAFT'),
    (1, 'PUBLISHED'),
    (2, 'BLAMED')
)


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    content = models.TextField(null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateField(auto_now_add=True, null=True)
    date_update = models.DateField(auto_now=True, null=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete= models.CASCADE,related_name='blog_posts', default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_created']
