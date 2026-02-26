import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.logging_config import setup_logger


def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", help="Price (required for LIMIT)")

    args = parser.parse_args()

    try:
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(float(args.quantity))
        validate_price(args.price, args.type)

        client = get_client()

        order = place_order(
    client,
    symbol=args.symbol,
    side=args.side,
    order_type=args.type,
    quantity=float(args.quantity),
    price=float(args.price) if args.price else None,
)

        print("\n===== ORDER SUMMARY =====")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")

        print("\n===== ORDER RESPONSE =====")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice')}")

        print("\n✅ Order placed successfully!")

    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()