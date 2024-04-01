from django.db import models
from django_resized import ResizedImageField

# Create your models here.
class Review(models.Model):
    ImagePeople = ResizedImageField (
        verbose_name='Изображение',
        force_format='WEBP',
        quality=75,
        upload_to='review',
    )
    name_surname = models.CharField(verbose_name='Имя Фамилия', max_length=50)
    main_review = models.TextField(verbose_name='Отзыв')

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'
    
    def __str__(self):
        return self.name_surname