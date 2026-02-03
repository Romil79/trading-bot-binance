import logging


class OrderManager:

    def __init__(self, client):
        self.client = client

    def create_order(self, symbol, side, order_type, qty, price=None):

        try:

            data = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": qty
            }

            if order_type == "LIMIT":
                data["price"] = price
                data["timeInForce"] = "GTC"

            result = self.client.place_order(data)

            logging.info(f"Order result: {result}")

            return result

        except Exception as e:

            logging.error(f"Order error: {e}")
            raise