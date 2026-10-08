# Forex Trading Bot

A Python-based automated Forex trading system designed for MetaTrader 5.

## Features

- MetaTrader 5 integration
- EMA 50 / EMA 200 trend filter
- RSI confirmation
- ATR-based stop loss
- Risk-based position sizing
- Spread protection
- Daily loss protection
- Maximum open trade protection
- Paper trading mode
- Live trading confirmation
- Emergency kill switch
- Automated tests

## WARNING

This software is not guaranteed to make money.

Forex trading involves substantial risk and can result in loss of capital.

Always test on a demo account before using real money.

## Installation

Clone the repository:

    git clone YOUR_GITHUB_REPOSITORY_URL

Enter the directory:

    cd forex-trading-bot

Create a virtual environment:

    python -m venv .venv

Activate it on Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

Install dependencies:

    pip install -r requirements.txt

## Configuration

Copy:

    .env.example

to:

    .env

Add your MetaTrader 5 demo account credentials.

Never upload `.env` to GitHub.

## Paper Trading

The default mode is:

    TRADING_MODE=paper

Run:

    python run_bot.py

The bot will generate signals but will NOT place real orders.

## Live Trading

Live trading requires BOTH:

    TRADING_MODE=live

and:

    ENABLE_LIVE_TRADING=true

The bot will additionally ask for:

    EXECUTE

before submitting each live order.

## Risk

Default risk per trade:

    0.5%

Default maximum daily loss:

    2%

Default maximum open positions:

    3

Default minimum reward/risk:

    2:1

These values can be changed in `.env`.

## Emergency Stop

Set:

    KILL_SWITCH=true

The bot will stop opening trades.

You can also stop the Python process with:

    CTRL+C

## Tests

Run:

    pytest

## Security

Never commit:

- MT5 passwords
- API keys
- `.env`
- account credentials

The `.gitignore` file already excludes `.env`.

## Strategy

The initial strategy uses:

- EMA 50
- EMA 200
- RSI 14
- ATR 14

A BUY signal requires:

- Price above EMA 200
- EMA 50 above EMA 200
- RSI between 50 and 68

A SELL signal requires:

- Price below EMA 200
- EMA 50 below EMA 200
- RSI between 32 and 50

Trades without valid risk parameters are rejected.

## Disclaimer

Past performance does not guarantee future results.

Automated Forex trading involves substantial financial risk.
