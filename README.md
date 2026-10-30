# Order Confirmation SAP Automation

A Python portfolio implementation for extracting and validating supplier order-confirmation details, with a configurable SAP GUI Scripting adapter interface.

> Scope note: This repository is a reconstructed portfolio implementation. The extraction and required-field validation logic are implemented. SAP transaction entry, Outlook/email processing, Excel integration, and a Tkinter desktop application are not included in the current source tree.

## Business problem

Order confirmations are often processed manually: a buyer searches for a supplier response, identifies the acknowledgement number, delivery date, price, and delivery address, and then enters the information into SAP. Manual re-keying is repetitive and makes validation and traceability harder.

This project documents a safe automation design for that workflow while keeping system-specific SAP field configuration separate from reusable parsing logic.

## Current implementation status

| Capability | Status |
| --- | --- |
| Extract acknowledgement number | Implemented with regular expressions |
| Extract delivery date | Implemented with regular expressions |
| Extract price | Implemented with regular expressions |
| Extract delivery address | Implemented with regular expressions |
| Required-field validation | Implemented; checks for missing values |
| SAP GUI transaction entry | Placeholder only; intentionally not implemented |
| Source-email attachment | Placeholder only; intentionally not implemented |
| Outlook email search | Not included |
| Excel integration | Not included |
| Tkinter desktop application | Not included |

## Intended manual process

1. Search supplier emails for an order confirmation.
2. Read the acknowledgement number, delivery date, price, and delivery address.
3. Enter the values into the relevant SAP transaction.
4. Attach the source email for traceability.
5. Check that required fields are complete.

## Automation design

The reusable part of the workflow is separated into small steps:

1. Receive confirmation text from an approved source.
2. Extract known labelled fields into an `OrderConfirmation` object.
3. Validate that required values are present.
4. Pass the validated object to a system-specific SAP adapter.
5. Attach the source email only after the target SAP workflow has been configured and tested.

The current repository stops after extraction and required-field validation. The SAP adapter deliberately raises `NotImplementedError` until SAP field selectors and transaction behavior are configured for the target system.

```text
Confirmation text
       |
       v
Field extraction -> OrderConfirmation -> Required-field validation
                                             |
                                             v
                              Future SAP GUI adapter and attachment flow
```

## Verified features

The current source code provides:

- `OrderConfirmation`, a dataclass containing the four extracted values.
- Case-insensitive extraction for acknowledgement/confirmation number, delivery date, price, and delivery address labels.
- `validate_confirmation`, which reports missing required values.
- `SapGuiAdapter`, an explicit integration boundary for future SAP GUI Scripting work.

## Technologies

- Python 3.10 or later
- Python standard library: `dataclasses` and `re`
- SAP GUI Scripting adapter interface only; system-specific selectors are not present
- Pytest for the portable unit tests

## Installation

Create a virtual environment and install the project with its test dependency:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

The current parser has no SAP, Outlook, Excel, or production-data dependency. Those systems must not be connected during parser-only testing.

## Usage example

```python
from extract_order_confirmations import extract_order_confirmation, validate_confirmation

text = """Acknowledgement number: ACK-123
Delivery date: 2026-11-01
Total price: USD 1,250.00
Delivery address: Plant 1, Bengaluru"""

confirmation = extract_order_confirmation(text)
errors = validate_confirmation(confirmation)

if errors:
    print("Validation errors:", errors)
else:
    print(confirmation)
```

## Testing

Run the portable unit tests from the repository root:

```powershell
python -m pytest
```

GitHub Actions runs the same test suite on Python 3.10 and 3.12 for pushes and pull requests targeting `main`.

## Error handling and logging

- Missing extracted values are returned as readable validation messages.
- SAP integration methods currently raise `NotImplementedError` to prevent accidental use before system-specific configuration is supplied.
- The current parser does not write files, connect to SAP, access Outlook, or modify production data.
- Application logging is not yet implemented; logging should be added when an external-system workflow is introduced.

## Benefits and reported results

The intended benefits are less repetitive re-keying, earlier detection of missing fields, and better traceability when a source email is attached to the SAP record.

`PROJECT_DETAILS.md` records reported workflow results of approximately 3–5 minutes reduced to 20–30 seconds per confirmation and approximately 95% accuracy. The repository does not contain benchmark scripts, raw measurements, or test evidence for those figures, so they should be treated as reported business context rather than independently verified project metrics.

## Known limitations

- The parser is line-oriented and regex-based; it is not an email parser or document-understanding model.
- Dates and prices are currently stored as strings and are not type-checked.
- The SAP adapter does not contain field IDs or transaction commands.
- Outlook, Excel, email attachment, and Tkinter workflows are not included.
- No production SAP or supplier data is bundled with this project.

## Future improvements

- Add strict date and decimal-price validation after the expected formats are confirmed.
- Add redacted email fixtures covering supplier template variations.
- Implement a dry-run SAP adapter that verifies intended field mappings without saving changes.
- Add structured logging and controlled recovery for SAP GUI session failures.
- Add system-specific integration tests only in an approved, non-production environment.
- Add screenshots or a short demonstration using fully synthetic data.

## Security and data handling

Do not commit supplier emails, company workbooks, SAP credentials, screenshots containing business data, or local file paths. Use synthetic or fully redacted fixtures for demonstrations. Authentication and system configuration should remain outside source code.

## Recruiter summary

This project demonstrates procurement process analysis, Python data extraction, structured validation, automation boundary design, and awareness of the controls required before connecting an automation to SAP. It presents the reusable foundation separately from system-specific transaction behavior rather than claiming an unverified end-to-end integration.
