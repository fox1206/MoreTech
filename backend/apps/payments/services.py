import urllib.parse

import httpx


API_BASE_URL = "https://hackathon.lsp.team/hk"


def new_wallet():
	url = urllib.parse.urljoin(API_BASE_URL, '/v1/wallets/new')
	wallet_json = httpx.get(url).json()
	return wallet_json['private_key'], wallet_json['public_key']


def new_transaction(sender, receiver, amount):
	url = urllib.parse.urljoin(API_BASE_URL, '/v1/transfers/matic')
	data = {
		"fromPrivateKey": sender,
		"toPublicKey": receiver,
		"amount": amount
	}
	transaction_json = httpx.post(url, data=data).json()
	return transaction_json['transactionHash']