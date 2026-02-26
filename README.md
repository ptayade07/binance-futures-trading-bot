# Binance Futures Testnet Trading Bot

## Overview

This is a simplified Python trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

The application is structured with separate layers for:
- Binance client configuration
- Order execution logic
- Input validation
- Logging configuration
- CLI interface

It supports BUY and SELL orders and logs all API requests, responses, and errors.

---

## Python Version

Tested with:

Python 3.11.x

(Note: Python 3.13+ may cause compatibility issues with some dependencies.)

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd trading_bot
```

### 2. Create Virtual Environment (Python 3.11 recommended)

```bash
py -3.11 -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

Make sure keys are generated from Binance Futures Testnet.

Base URL used:
https://testnet.binancefuture.com

---

## How to Run

### MARKET Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### LIMIT Order Example

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 80000
```

---

## Output

The application prints:

- Order Summary
- Order ID
- Status
- Executed Quantity
- Average Price
- Success / Failure message

---

## Logging

All API interactions are logged in:

```
logs/trading_bot.log
```

Logs include:
- Order request details
- API response
- Errors (if any)

---

## Assumptions

- Binance Futures Testnet account is active.
- Minimum notional requirement for BTCUSDT Futures is 100 USDT.
- Python 3.11 recommended for compatibility.