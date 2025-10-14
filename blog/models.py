from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from unidecode import unidecode
from ckeditor_uploader.fields import RichTextUploadingField  # CKEditor с загрузкой файлов

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = 'PB', 'Опубликовано'
        DRAFT = 'DF', 'Черновик'

    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, verbose_name='Категория')
    tags = models.ManyToManyField(to='Tag', blank=True)
    content = RichTextUploadingField(verbose_name='Содержание')  # теперь можно вставлять картинки прямо в текст
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Автор')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата публикации')
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name='Статус'
    )

    objects = models.Manager()
    published = PublishedManager()

    def save(self, *args, **kwargs):
        # Если статус меняется на "Опубликовано" и дата публикации еще не установлена — ставим текущее время
        if self.status == self.Status.PUBLISHED and self.published_at is None:
            self.published_at = timezone.now()

        # Если статус изменился на "Черновик" — сбрасываем дату публикации (по желанию)
        elif self.status == self.Status.DRAFT:
            self.published_at = None

        # Автоматическая генерация slug
        if not self.slug:
            base_slug = slugify(unidecode(self.title))
            slug = base_slug
            counter = 1

            # Проверяем уникальность slug
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.slug])
    

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ["-published_at"]
        indexes = [models.Index(fields=['-published_at'])]


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_list_by_category", args=[self.slug])
    

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'