from django.db.models.signals import post_save
from django.dispatch import receiver

from ..account.models import Account
from .models import Wallet
from .services import new_wallet


@receiver(post_save, sender=Account)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        private_key, public_key = new_wallet()
        Wallet.objects.create(
            user=instance,
            private_key=private_key,
            public_key=public_key
        )