from extract_order_confirmations import (
    OrderConfirmation,
    extract_order_confirmation,
    validate_confirmation,
)


def test_extracts_supported_fields():
    text = """Acknowledgement number: ACK-123
Delivery date: 2026-11-01
Total price: USD 1,250.00
Delivery address: Plant 1, Bengaluru"""

    result = extract_order_confirmation(text)

    assert result == OrderConfirmation(
        acknowledgement_number="ACK-123",
        delivery_date="2026-11-01",
        price="USD 1,250.00",
        delivery_address="Plant 1, Bengaluru",
    )


def test_supports_confirmation_number_alias():
    result = extract_order_confirmation("Confirmation #: CNF-9")

    assert result.acknowledgement_number == "CNF-9"


def test_reports_missing_required_values():
    item = OrderConfirmation(acknowledgement_number="ACK-1", price="USD 10")

    assert validate_confirmation(item) == [
        "Missing delivery date",
        "Missing delivery address",
    ]


def test_empty_input_reports_all_required_values():
    item = extract_order_confirmation("")

    assert item == OrderConfirmation()
    assert validate_confirmation(item) == [
        "Missing acknowledgement number",
        "Missing delivery date",
        "Missing price",
        "Missing delivery address",
    ]
