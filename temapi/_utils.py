from typing import Any, Dict


def build_url(base: str, args: Dict[str, Any]):
    params = list()

    for key, value in args.items():
        value = "" if value is None else value
        params.append(f"{key}={value}")

    if len(params) > 0:
        qs = "&".join(params)
        return f"{base}?{qs}"
    else:
        return base


def payment(price: int, amount: int, duration: int) -> int:
    """
    Calculate the total payment for an order based on price, amount, and duration.

    Args:
        price (int): The price per unit of resource.
        amount (int): The amount of resource being ordered.
        duration (int): The duration for which the resource is being ordered.

    Returns:
        int: The total payment required for the order.
    """
    return int(
        (price * amount * (duration + (86400 if duration < 86400 else 0))) / 86400
    )
