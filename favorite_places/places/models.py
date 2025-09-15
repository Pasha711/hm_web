# places/models.py

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Place(models.Model):
    """Модель для зберігання інформації про улюблене місце."""
    name = models.CharField(max_length=200, verbose_name="Назва")
    description = models.TextField(verbose_name="Опис")
    place_type = models.CharField(max_length=100, verbose_name="Тип місця")
    location = models.CharField(max_length=200, blank=True, null=True, verbose_name="Локація")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Рейтинг"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    # Поле для прив'язки до сесії користувача
    session_key = models.CharField(max_length=40, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Місце"
        verbose_name_plural = "Місця"
        ordering = ['-created_at']