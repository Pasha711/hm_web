from django.db import models
from django.urls import reverse

# Модель для зберігання контента головної сторінки
class MainPage(models.Model):
    title = models.CharField("Заголовок", max_length=200, default="Головна сторінка")
    description = models.TextField("Опис факультету")
    contact_info = models.TextField("Контактна інформація")

    class Meta:
        verbose_name = "Головна сторінка"
        verbose_name_plural = "Головна сторінка"

    def __str__(self):
        return self.title

# Модель "Кафедра"
class Department(models.Model):
    name = models.CharField("Назва кафедри", max_length=200)
    head_of_department = models.CharField("Завідувач кафедрою", max_length=150)

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедри"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('department_detail', kwargs={'pk': self.pk})

# Модель "Спеціальність"
class Program(models.Model):
    name = models.CharField("Назва спеціальності", max_length=200)
    code = models.CharField("Код спеціальності", max_length=50)
    description = models.TextField("Повний опис")
    coordinator_name = models.CharField("Ім'я координатора набору", max_length=150)
    coordinator_contact = models.CharField("Контакт координатора набору", max_length=200)
    graduating_department = models.ForeignKey(
        Department, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='programs',
        verbose_name="Випускаюча кафедра"
    )
    disciplines = models.TextField("Список дисциплін", help_text="Перерахуйте дисципліни через кому")

    class Meta:
        verbose_name = "Спеціальність"
        verbose_name_plural = "Спеціальності"

    def __str__(self):
        return f"{self.code} {self.name}"

    def get_absolute_url(self):
        return reverse('program_detail', kwargs={'pk': self.pk})
    
    def get_short_description(self):
        """Повертає перші 50 слов опису."""
        words = self.description.split()
        return ' '.join(words[:50]) + ('...' if len(words) > 50 else '')

# Модель "Викладач"
class Teacher(models.Model):
    name = models.CharField("Ім'я викладача", max_length=150)
    position = models.CharField("Посада", max_length=100)
    degree = models.CharField("Науковий ступінь", max_length=100)
    department = models.ForeignKey(
        Department, 
        on_delete=models.CASCADE, 
        related_name='teachers',
        verbose_name="Кафедра"
    )

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"

    def __str__(self):
        return self.name
