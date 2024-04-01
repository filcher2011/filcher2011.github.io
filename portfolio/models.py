from django.db import models
from django_resized import ResizedImageField
from django.utils import timezone

class Portfolio(models.Model):
    img_portfolio = ResizedImageField (
        verbose_name='Изображение',
        force_format='WEBP',
        quality=75,
        upload_to='portfolio',
    )
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    descriptions = models.TextField(verbose_name='Описание')
    relise = models.DateField(verbose_name='Релиз', default=timezone.now)
    typepor = models.CharField(verbose_name='Тип', max_length=50, default='Program')

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
    
    def __str__(self):
        return self.title