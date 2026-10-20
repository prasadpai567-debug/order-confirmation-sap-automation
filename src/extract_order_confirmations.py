"""Extract and validate order-confirmation details."""
from dataclasses import dataclass
import re

@dataclass
class OrderConfirmation:
    acknowledgement_number: str = ""
    delivery_date: str = ""
    price: str = ""
    delivery_address: str = ""

def _find(pattern: str, text: str) -> str:
    match = re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE)
    return match.group(1).strip() if match else ""

def extract_order_confirmation(text: str) -> OrderConfirmation:
    return OrderConfirmation(
        acknowledgement_number=_find(r"(?:acknowledgement|acknowledgment|confirmation)\s*(?:number|no\.?|#)\s*[:\-]?\s*(.+)", text),
        delivery_date=_find(r"delivery\s*date\s*[:\-]?\s*(.+)", text),
        price=_find(r"(?:total\s*)?price\s*[:\-]?\s*(.+)", text),
        delivery_address=_find(r"delivery\s*address\s*[:\-]?\s*(.+)", text),
    )

def validate_confirmation(item: OrderConfirmation) -> list[str]:
    values = {
        "acknowledgement_number": item.acknowledgement_number,
        "delivery_date": item.delivery_date,
        "price": item.price,
        "delivery_address": item.delivery_address,
    }
    return [f"Missing {name.replace('_', ' ')}" for name, value in values.items() if not value]
