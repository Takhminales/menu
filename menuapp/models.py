from django.db import models
from django.urls import reverse, NoReverseMatch


class Menu(models.Model):
    """Например: main_menu, footer_menu, sidebar_menu"""
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    Один пункт меню.
    parent   – ссылка на родителя (NULL для корневых пунктов)
    menu     – к какому меню принадлежит
    url      – либо явный путь ( /about/ ), либо name из urls.py
    is_named – флаг: url — это name, а не прямой путь
    order    – ручная сортировка внутри одного уровня
    """
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    parent = models.ForeignKey(
        'self',
        null=True, blank=True,
        related_name='children',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=120)
    url = models.CharField(max_length=200, help_text="'/about/'  или  'about' для named-url")
    is_named = models.BooleanField(
        default=False,
        help_text="Отметьте, если url — это name из urls.py"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('order',)
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return self.title

    # единственная точка, где хардкод мог бы появиться,
    # но мы динамически пытаемся зареверсить
    def get_url(self):
        if self.is_named:
            try:
                return reverse(self.url)
            except NoReverseMatch:
                return '#'
        return self.url or '#'
