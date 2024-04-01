from django.db import models

# Create your models here.
class Services(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50, default='ProductName')
    price = models.IntegerField(verbose_name='Цена', default=1000)
    firstDop = models.CharField(verbose_name='Первый плюс', max_length=30, default='√ Качественно и быстро')
    secondDop = models.CharField(verbose_name='Второй плюс', max_length=30, default='√ Качественно и быстро')
    thirdDop = models.CharField(verbose_name='Третий плюс', max_length=30, default='√ Качественно и быстро')
    fourdDop = models.CharField(verbose_name='Четвертый плюс', max_length=30, default='√ Качественно и быстро')

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'
    
    def __str__(self):
        return self.title