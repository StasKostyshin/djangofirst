from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField('Название', max_length=50)
    file = models.FileField(upload_to="video/", null=True, blank=True)
    date = models.DateTimeField('Дата публикации')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видеофайлы'
