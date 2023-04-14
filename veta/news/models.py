from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

