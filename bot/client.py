import os
from pathlib import Path
from dotenv import load_dotenv
from binance.client import Client

# Explicitly load .env from project root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("API Key or Secret not found in .env file")

    client = Client(api_key, api_secret)

    # Futures Testnet URL
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client