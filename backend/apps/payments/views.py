from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

from ..base.permissions import IsAuthor
from .models import Transaction, Wallet
from .services import new_transaction
from .serializers import TransactionSerializer


class TransactionView(ModelViewSet):
	serializer_class = TransactionSerializer

	def get_queryset(self):
		user = self.request.user
		queryset = Transaction.objects.filter(
			Q(sender=user) | Q(receiver=user)
		)
		return queryset

	def perform_create(self, serializer):
		sender_hash = self.request.user.wallet.private_key
		receiver = serializer.validated_data.get('receiver')
		amount = serializer.validated_data.get('amount')

		receiver_wallet = Wallet.objects.get(user=receiver)
		transaction_hash = new_transaction(sender_hash, receiver_wallet.private_key, amount)

		serializer.save(
			sender=sender,
			receiver=receiver,
			transaction_hash=transaction_hash,
			amount=amount
		)


class TransactionDetailView(ModelViewSet):
	pass