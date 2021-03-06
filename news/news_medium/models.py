from django.db import models
from embed_video.fields import EmbedVideoField
from django.urls import reverse




class Author(models.Model):
    '''
    Author posts
    '''
    name = models.CharField(max_length=30)
    sur_name = models.CharField(max_length=30)
    about_me = models.TextField(blank=True, default='Good author!')

    def __str__(self):
        return f'{self.name} {self.sur_name}'


class CategoryArticle(models.Model):
    name_category = models.CharField(max_length=30)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name_category}'

    class Meta:
        ordering = ('-create',)


class Article(models.Model):
    '''
    Posts from main page
    '''
    STATUS_CHOISE = (
        ('draft', 'Draft'),
        ('publisher', 'Publisher'),
    )
    title = models.CharField(max_length=250)
    text = models.TextField(blank=False, default='')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blog_posts')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Photo')
    last_change = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250)
    status = models.CharField(max_length=10, choices=STATUS_CHOISE, default='draft')
    video = EmbedVideoField(blank=True, verbose_name='Video')
    category = models.ForeignKey(CategoryArticle, on_delete=models.CASCADE, related_name='tag')

    class Meta:
        ordering = ('-create',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('one_article', kwargs={'slug': self.slug})


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    comment_text = models.TextField()
    comment_create = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('comment_create',)

    def __str__(self):
        return f'Comment by {self.name} on {self.article}'

    def get_absolute_url(self):
        return f'/article/{self.article}/add_comment/'
