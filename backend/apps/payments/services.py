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


def ruble_transaction(sender, receiver, amount):
	url = urllib.parse.urljoin(API_BASE_URL, '/hk/v1/transfers/ruble')
	headers = {
		"Content-Type": "application/json",
		"Accept": "application/json"
	}
	data = {
		"fromPrivateKey": sender,
		"toPublicKey": receiver,
		"amount": float(amount)
	}
	transaction_json = httpx.post(url, data=data).json()
	return transaction_json['transaction']


def get_balance(public_key):
	url = urllib.parse.urljoin(
		API_BASE_URL,
		f'/hk/v1/wallets/{public_key}/balance'
	)
	headers = {
		"Accept": "application/json"
	}
	balance_json = httpx.get(url, headers=headers).json()
	return balance_json


def get_balance_history(public_key):
	pass


def get_status(transaction_hash):
	url = urllib.parse.urljoin(
		API_BASE_URL,
		f'/hk/v1/transfers/status/{transactionHash}'
	)
	headers = {
		"Accept": "application/json"
	}
	status_json = httpx.get(url, headers=headers).json()
	return status_json
