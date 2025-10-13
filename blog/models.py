from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from unidecode import unidecode

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
    content = models.TextField(verbose_name='Содержимое')
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
        # Если статус поменялся на "Опубликовано" и дата публикации еще не установлена — ставим текущее время
        if self.status == self.Status.PUBLISHED and self.published is None:
            self.published = timezone.now()

        # Если статус изменился на "Черновик", сбрасываем дату публикации (опционально)
        elif self.status == self.Status.DRAFT:
            self.published = None

        # Автоматическая генерация slug
        if not self.slug:
            counter = 1
            slug = slugify(unidecode(self.title))

            # Проверяем уникальность slug
            while Post.objects.filter(slug=slug).exists():
                slug = f"{slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'