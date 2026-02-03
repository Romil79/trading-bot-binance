# Binance Futures Trading Bot (Testnet)

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

### Market Order

python main.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001

### Limit Order

python main.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 70000

## Features

- Place Market and Limit orders
- Input validation
- Error handling
- Logging

## Assumptions

- Using Binance Futures Testnet
- Only USDT-M pairs supported
- For learning purpose