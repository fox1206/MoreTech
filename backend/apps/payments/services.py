import urllib.parse

import httpx


API_BASE_URL = "https://hackathon.lsp.team/"


def new_wallet():
	url = urllib.parse.urljoin(API_BASE_URL, '/hk/v1/wallets/new')
	headers = {
		"Accept": "application/json"
	}
	wallet_json = httpx.post(url, headers=headers).json()
	return wallet_json['privateKey'], wallet_json['publicKey']


def new_transaction(sender, receiver, amount):
	url = urllib.parse.urljoin(API_BASE_URL, '/hk/v1/transfers/matic')
	headers = {
		"Content-Type": "application/json",
		"Accept": "application/json"
	}
	data = {
		"fromPrivateKey": sender,
		"toPublicKey": receiver,
		"amount": amount
	}
	transaction_json = httpx.post(url, data=data).json()
	return transaction_json['transactionHash']


def get_balance(public_key):
	url = urllib.parse.urljoin(
		API_BASE_URL,
		f'/hk/v1/wallets/{public_key}/balance'
	)
	headers = {
		"Accept": "application/json"
	}
	print(url)
	balance_json = httpx.get(url, headers=headers).json()
	return balance_json
