from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    """Создаем модель поста в блоге"""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """Атрибут, позволяющий использовать форму в том виде, как написано ниже """
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.title


class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Атрибут, позволяющий использовать форму в том виде, как написано ниже  """
        verbose_name = 'запись'
        verbose_name_plural = 'записи'

    def __str__(self):
        """Возвращает строковое представление модели."""
        if len(self.text) <= 50:
            return self.text
        return self.text[:50] + "..."
