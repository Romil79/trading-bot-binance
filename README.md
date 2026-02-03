# Binance Futures Trading Bot (Testnet)

<<<<<<< HEAD
This is a simple Python project to place orders on Binance Futures Testnet.

It supports Market and Limit orders using command line.

## Setup

1. Install dependencies

pip install -r requirements.txt

2. Set API keys

export BINANCE_API_KEY=your_api_key
export BINANCE_API_SECRET=your_secret_key

3. Create logs folder (if not present)

mkdir logs

## Run
=======
This project is a simple Python application to place orders on Binance Futures Testnet.
It was created as part of an internship assignment.

The bot supports Market and Limit orders using command line.


## Features

- Place Market and Limit orders
- Buy and Sell support
- Input validation
- Error handling
- Logging of API requests and responses


## Requirements

- Python 3.8+
- Binance Futures Testnet account
- API Key and Secret


## Setup

1. Clone the repository

git clone <your-repo-link>

2. Create virtual environment

python -m venv venv

3. Activate environment

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

5. Set API keys (PowerShell)

$env:BINANCE_API_KEY="your_api_key"
$env:BINANCE_API_SECRET="your_secret"


## Run Examples
>>>>>>> 5f86265f092c018e1881760e487353731efcf6f5

### Market Order

python main.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001

### Limit Order

python main.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 70000

<<<<<<< HEAD
## Features

- Place Market and Limit orders
- Input validation
- Error handling
- Logging

## Assumptions

- Using Binance Futures Testnet
- Only USDT-M pairs supported
- For learning purpose
=======

## Project Structure

trading_bot/
- main.py
- binance_client.py
- order_manager.py
- validators.py
- logger.py

---

## Logs

All API requests and responses are stored in:

logs/app.log

---

## Notes

- This project uses Binance Futures Testnet (not real money).
- It is created for learning and practice purpose.
>>>>>>> 5f86265f092c018e1881760e487353731efcf6f5
