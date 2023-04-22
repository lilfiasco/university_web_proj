from django.db import models
from auths.models import CustomUser


class Furniture(models.Model):
    """Furniture (single object)."""

    title = models.CharField(
        max_length=50,
        verbose_name='название'
    )
    room = models.ForeignKey(
        'Rooms',
        on_delete=models.CASCADE,
        verbose_name='интерьер для'
    )
    price = models.PositiveIntegerField(
        verbose_name='цена'
    )
    image = models.ImageField(
        verbose_name="изображение",
        upload_to="images/"
    )
    url = models.SlugField(
        max_length=160, 
        unique=True,
        null=False
    )


    class Meta:
        ordering = [
            '-id'
        ]
        verbose_name = 'мебель'
        verbose_name_plural = 'мебель'

    def __str__(self) -> str:
        return self.title
    


class Rooms(models.Model):
    """Rooms for furniture sections."""

    title = models.CharField(
        max_length=75,
        verbose_name='название'
    )

    url = models.SlugField(
        max_length=160, 
        unique=True,
        null=False
    )


    class Meta:
        ordering = [
            '-id'
        ]
        verbose_name = 'комната'
        verbose_name_plural = 'комнаты'

    def __str__(self) -> str:
        return self.title


class Favs(models.Model):
    """Favs of products.""" 

    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE
    )
    furniture = models.ForeignKey(
        Furniture, 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "избранное"
        verbose_name_plural = "избранные"

    def __str__(self) -> str:
        return self.user.email

    # def check(self):
    #     print("FAAAAAAAAAAAAVS:   ", self.user, self.furniture)
        # return self.furniture


class Basket(models.Model):
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE
    )
    furniture = models.ForeignKey(
        Furniture, 
        on_delete=models.CASCADE
    )
    price = models.FloatField('Цена')
    quantity_buying = models.IntegerField('Общее количество')

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self) -> str:
        return self.user.email

    def sum(self):
        print("FFFFFFFFF:   ", self.price, self.quantity_buying)
        return self.price * self.quantity_buying


class Card(models.Model):
    name = models.CharField("Банковская карта", max_length=255, unique=True )

    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карты"

    def __str__(self) -> str:
        return self.name


class Pay(models.Model):
    name = models.CharField("Способ оплаты", max_length=255, unique=True )

    class Meta:
        verbose_name = "Способ оплаты"
        verbose_name_plural = "Способы оплаты"

    def __str__(self) -> str:
        return self.name


class Buy(models.Model):
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE
    )
    purchased_furnitures = models.ManyToManyField(
        to=Furniture
    )
    date = models.SmallIntegerField("Дата покупки")
    total_price = models.FloatField()
    total_buying = models.ForeignKey(
        Basket, 
        on_delete=models.CASCADE
    )
    card = models.ForeignKey(
        Card, 
        on_delete=models.CASCADE
    )
    pay = models.ForeignKey(
        Pay, 
        on_delete=models.CASCADE
    )

