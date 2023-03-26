from django.db import models
from members.models import Member
import uuid


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.TextField(max_length=500, null=True, blank=True)
    category_slug = models.SlugField(max_length=20, unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.category_name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Topic(models.Model):
    # topic_uuid = models.UUIDField(default = uuid.uuid4, editable=False)
    topic_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    topic_title = models.CharField(max_length=200)
    topic_opened_by = models.ForeignKey(Member, on_delete=models.CASCADE)
    topic_date = models.DateTimeField(auto_now_add=True)
    topic_slug = models.SlugField(max_length=20, unique=True, null=True, blank=True)

    def topic_posts_count(self):
        return Post.objects.filter(post_topic=self.pk).count()

    def __str__(self):
        return f"{self.topic_category} | {self.topic_opened_by} | {self.topic_title} | {self.topic_posts_count()}"



class Post(models.Model):
    post_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    post_user = models.ForeignKey(Member, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now=True)
    post_content = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.post_user} | {self.post_topic} | {self.post_content[:30]}"