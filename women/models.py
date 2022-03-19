from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    # slug = models.SlugField(max_length=255, unique=True,
    #                         db_index=True, verbose_name='URL', blank=True)
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    # photo = models.ImageField(
    #     upload_to="photos/%Y/%m/%d/", verbose_name='Фото', blank=True)
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(
        auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey(
        'Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(
        max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    # def str(self):
    #     return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
