from rest_framework import serializers

from . import models
from ..account.serializers import UserSerializer


class TransactionSerializer(serializers.ModelSerializer):
    transaction_hash = serializers.ReadOnlyField()

    class Meta:
        model = models.Transaction
        fields = [
            "id",
            # "sender",
            "receiver",
            "amount",
            "transaction_hash"
        ]


class BalanceSerializer():
    pass
