from django.db import models


class Furniture(models.Model):
    """Furniture (single object)."""

    title = models.CharField(
        max_length=50,
        verbose_name='название'
    )
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        verbose_name='производитель'
    )
    room_belonging = models.ForeignKey(
        'Rooms',
        on_delete=models.CASCADE,
        verbose_name='интерьер для'
    )
    price = models.PositiveIntegerField(
        verbose_name='цена'
    )


    class Meta:
        ordering = [
            '-id'
        ]
        verbose_name = 'мебель'
        verbose_name_plural = 'мебель'

    def __str__(self) -> str:
        return self.title
    

class Company(models.Model):
    """Companies."""

    title = models.CharField(
        max_length=75,
        verbose_name='название'
    )


    class Meta:
        ordering = [
            '-id'
        ]
        verbose_name = 'компания'
        verbose_name_plural = 'компании'

    def __str__(self) -> str:
        return self.title


class Rooms(models.Model):
    """Rooms for furniture sections."""

    title = models.CharField(
        max_length=75,
        verbose_name='название'
    )


    class Meta:
        ordering = [
            '-id'
        ]
        verbose_name = 'комната'
        verbose_name_plural = 'комнаты'

    def __str__(self) -> str:
        return self.title
