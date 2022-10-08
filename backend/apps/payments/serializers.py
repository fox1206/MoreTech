from rest_framework import serializers

from . import models


class TransactionSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField()

    class Meta:
        model = models.Transaction
        fields = [
            "sender",
            "receiver",
            "amount"
        ]