from django.db import models
from django.contrib.auth.models import User


# Модель для сущности "Продукт"
class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Модель для сущности "Доступ к продукту для пользователя"
class UserProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


# Модель для сущности "Урок"
class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.URLField()
    duration_seconds = models.IntegerField()

    def __str__(self):
        return self.name


# Модель для сущности "Фиксация времени просмотра урока пользователем"
class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
    view_time_seconds = models.IntegerField()
    view_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} просмотрел урок {self.lesson} ({self.view_date})"
