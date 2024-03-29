from django.contrib.auth.models import User
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children')
    slug = models.SlugField(max_length=100, unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель товара"""
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=150)
    description = models.TextField('Описание')
    price = models.IntegerField('Цена', default=0)
    product_code = models.CharField('Код товара', max_length=13)
    slug = models.SlugField(max_length=150)
    availability = models.BooleanField('Наличие', default=True)
    quantity = models.IntegerField('Количество', default=1)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


class Cart(models.Model):
    """Корзина"""
    user = models.ForeignKey(User, verbose_name='Покупатель', on_delete=models.CASCADE)
    accepted = models.BooleanField(verbose_name='Принято к заказу', default=False)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return '{}'.format(self.user)


class CartItem(models.Model):
    """Товары в корзине"""
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Корзина', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Количество', default=0)

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def __str__(self):
        return '{}'.format(self.cart)


class Order(models.Model):
    """Заказы"""
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE)
    accepted = models.BooleanField(verbose_name='Заказ выполнен', default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return '{}'.format(self.cart)