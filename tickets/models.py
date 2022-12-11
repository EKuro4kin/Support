from django.db import models

from users.models import User


class Ticket(models.Model):

    class Status(models.IntegerChoices):
        to_do = 1, "Не решенный"
        done = 2, "Решённый"
        frozen = 3, "Замороженный"

    class Meta:
        verbose_name = "Тикет"
        verbose_name_plural = "Тикеты"

    question_name = models.CharField(verbose_name="Название вопроса", unique=True, max_length=100)
    description = models.CharField(verbose_name="Описание", max_length=255)
    answer = models.TextField(verbose_name="Ответ", null=True)
    status = models.PositiveSmallIntegerField(
        verbose_name="Статус", choices=Status.choices, default=Status.to_do
    )


class TicketComment(models.Model):
    class Meta:
        verbose_name = "Сообщение к тикету"
        verbose_name_plural = "Сообщения к тикету"

    text = models.TextField(verbose_name="Текс сообщения")
    ticket = models.ForeignKey(Ticket, verbose_name="Тикет", on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, related_name="comments")