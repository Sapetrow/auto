from django.db import models

# Create your models here.
class Auto(models.Model):
    number = models.CharField(max_length=15, verbose_name='Государственный номер')
    marka = models.CharField(max_length=50, verbose_name='Марка')
    model = models.CharField(max_length=50, verbose_name='Модель')
    vin = models.CharField(max_length=17, verbose_name='ВИН номер')
    #publish=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')

    class Meta:
        verbose_name_plural = 'Автомобили'
        verbose_name = 'Автомобиль'
        ordering = ['number']

class Client(models.Model):
    lastname = models.CharField(max_length=15, verbose_name='Фамилия')
    firstname = models.CharField(max_length=15, verbose_name='Имя')
    middlename = models.CharField(max_length=15, verbose_name='Отчество')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона')
    adress = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'
        ordering = ['lastname']

class Product(models.Model):
    cod = models.CharField(max_length=10, verbose_name='Каталожный номер')
    nameproduct = models.CharField(max_length=20, verbose_name='Название товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Стоимость')

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['cod']

class Work(models.Model):
    cod = models.CharField(max_length=10, verbose_name='Каталожный номер')
    nameproduct = models.CharField(max_length=20, verbose_name='Название работы')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Стоимость')

    class Meta:
        verbose_name_plural = 'Работы'
        verbose_name = 'Работа'
        ordering = ['cod']

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, db_constraint=True,verbose_name='клиент')
    auto = models.ForeignKey(Auto, null=True, on_delete=models.PROTECT, db_constraint=True, verbose_name='Автомобиль')
    datepub = models.DateTimeField(auto_now=True)
    work=models.ManyToManyField(Work)#, through='Kit', through_fields=('order', 'work'))
    product=models.ManyToManyField(Product)

    class Meta:
        verbose_name_plural = 'Заказ-наряды'
        verbose_name = 'Заказ-наряд'

#class Kit(models.Model):
#    order=models.ForeignKey(Order, on_delete=models.CASCADE)
#    work=models.ForeignKey(Work, on_delete=models.CASCADE)
 #   count=models.IntegerField()




