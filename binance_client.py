import os
import logging
from binance.client import Client


class BinanceClient:

    def __init__(self):

        api_key = os.getenv("BINANCE_API_KEY")
        secret_key = os.getenv("BINANCE_API_SECRET")

        if not api_key or not secret_key:
            raise Exception("API key or Secret not found")

        self.client = Client(api_key, secret_key, testnet=True)

        # Set testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logging.info("Binance client initialized")

    def place_order(self, params):

        logging.info(f"Sending order: {params}")

        return self.client.futures_create_order(**params)