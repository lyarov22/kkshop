from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    denotation = models.CharField(max_length=200, db_index=True, null=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/', blank=True)
    description = models.TextField(blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    visible = models.BooleanField(default=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
    
    def img_preview(self):
        return mark_safe(f'<img src="{self.image.url}" width="300"/>')
    
    def get_old_price(self):
        return self.price
    
    def get_discount_price(self):
        discount_percent = (100 - self.discount) / 100
        return round(self.price * discount_percent, 2)
    
    def is_discounted(self):
        return self.discount > 0
    
    def is_recently_published(self):
        # Получаем текущую дату и время
        now = timezone.now()
        
        # Разница между текущей датой и временем и датой создания товара
        time_difference = now - self.created
        
        # Проверяем, прошло ли менее 30 дней с момента публикации товара
        return time_difference.days < 30