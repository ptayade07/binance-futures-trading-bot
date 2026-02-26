import logging
from binance.enums import *


def place_order(client, symbol, side, order_type, quantity, price=None):
    logger = logging.getLogger()

    try:
        logger.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_MARKET,
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logger.info(f"Order response: {order}")

        return order

    except Exception as e:
        logger.error(f"Error placing order: {e}")
        raise