from django.db import models

from django.contrib.auth.models import User


class Wallet(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
        related_name='wallet'
    )
    private_key = models.CharField(max_length=64)
    public_key = models.CharField(max_length=64)

    class Meta:
        verbose_name = "кошелек"
        verbose_name_plural = "кошельки"

    def __str__(self):
        return f'{self.user}'


class Transaction(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='отправитель',
        related_name='отправленные'
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='получатель',
        related_name='полученные'
    )
    transaction_hash = models.CharField(
        max_length=64
    )
    amount = models.DecimalField(
        'размер бонуса',
        max_digits=8,
        decimal_places=2,
        default=0
    )

    class Meta:
        verbose_name = "транзакция"
        verbose_name_plural = "транзакции"

    def __str__(self):
        return f'{self.sender} -> {self.receiver}'
