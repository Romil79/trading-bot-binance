import argparse
import logging

from logger import setup_logger
from binance_client import BinanceClient
from order_manager import OrderManager
from validators import *


def main():

    setup_logger()

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        check_side(args.side)
        check_type(args.type)
        check_quantity(args.qty)
        check_price(args.price, args.type)

        client = BinanceClient()
        manager = OrderManager(client)

        print("\nOrder Details")
        print("------------")
        print("Symbol:", args.symbol)
        print("Side:", args.side)
        print("Type:", args.type)
        print("Quantity:", args.qty)
        print("Price:", args.price)

        response = manager.create_order(
            args.symbol,
            args.side,
            args.type,
            args.qty,
            args.price
        )

        print("\nOrder Result")
        print("-----------")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice"))

        print("\nOrder placed successfully")

    except Exception as err:

        logging.exception("Error occurred")
        print("Error:", err)


if __name__ == "__main__":
    main()