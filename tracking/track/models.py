from django.db import models


class Type(models.Model):
    type = models.CharField('Тип', max_length=250)

    class Meta:
        ordering = ('type',)
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self) -> str:
        return self.type


class Order(models.Model):
    number = models.PositiveIntegerField("Номер заказа")
    date_time = models.DateTimeField("Дата сдачи заказа")
    type_order = models.ForeignKey(
        Type, verbose_name="Тип заказа", on_delete=models.SET_NULL, null=True
    )
    completeness = models.BooleanField("Заказ завершен", default=False)

    class Meta:
        ordering = ['date_time']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        indexes = [
            models.Index(fields=['date_time']),
        ]

    def __str__(self) -> str:
        return str(self.number)
