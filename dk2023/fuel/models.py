from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
        verbose_name="Nazwa")
    class Meta:
        ordering = ["name"]
        verbose_name = "Rodzaj paliwa"
        verbose_name_plural = "Rodzaj paliwa"

    def __str__(self):
        return self.name


class Fuel(models.Model):
    title = models.CharField(
        max_length=128,
        null=False,
        unique=False,
        verbose_name="Miasto/stacja")
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Cena")
    date_from = models.DateField(verbose_name="Data od")
#    date_to = models.DateField(verbose_name="Data do")
    description = models.TextField(
        blank=True,
        default="",
        verbose_name="Opis")
    class Statuses(models.TextChoices):
        AVAILABLE = "d", "Dostępna"
        NOT_AVAILABLE = "n", "Niedostępna"
    status = models.CharField(
        max_length=1,
        choices=Statuses.choices,
        default=Statuses.AVAILABLE)
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL)
    image = models.ImageField(
        upload_to="fuel",
        null=True,
        blank=True,
        verbose_name="Obraz")

    # owner = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     blank=True,)

    class Meta:
        verbose_name="Stacje i Cene"
        verbose_name_plural="Lista stacji"

    def __str__(self):
        return self.title