def check_side(side):

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")


def check_type(order_type):

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Type must be MARKET or LIMIT")


def check_quantity(qty):

    if qty <= 0:
        raise ValueError("Quantity should be greater than 0")


def check_price(price, order_type):

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT order")