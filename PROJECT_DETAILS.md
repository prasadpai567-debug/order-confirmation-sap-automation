# Order Confirmation Entries in SAP

## Portfolio scope

This repository is a reconstructed portfolio implementation for a procurement automation workflow. It separates reusable order-confirmation extraction and required-field validation from system-specific SAP GUI configuration.

## Business problem

Order confirmations were previously processed manually. The intended process involved searching supplier emails, identifying the acknowledgement number, delivery date, price, and delivery address, entering the values into SAP, and retaining the source email for traceability.

## Current implementation

The source tree currently implements:

- Regular-expression extraction of acknowledgement/confirmation number, delivery date, price, and delivery address.
- A structured OrderConfirmation dataclass for the extracted values.
- Required-field validation that reports missing values.
- A SapGuiAdapter boundary for future SAP GUI Scripting configuration.

## Not implemented in this repository

The following capabilities are described as future or system-specific work and are not currently implemented in the source tree:

- SAP transaction entry and save behavior.
- SAP field IDs or target-system selectors.
- Outlook email search or source-email attachment.
- Excel integration.
- Tkinter desktop user interface.
- Production-system integration testing.

The adapter methods intentionally raise NotImplementedError until they are configured and tested for an approved target system. This prevents the portfolio code from implying that an unconfigured SAP workflow is production-ready.

## Reported workflow results

The original workflow description reports the following business context:

- Processing time reported as approximately 3–5 minutes reduced to 20–30 seconds per confirmation.
- Approximately 95% accuracy based on reported workflow results.
- Less repetitive manual entry.
- Better traceability through source-email attachment.

The repository does not contain benchmark scripts, raw measurements, accuracy calculations, or end-to-end test evidence for these figures. They should therefore be treated as reported context, not independently verified project metrics.

## Contribution

I identified the improvement opportunity and contributed the Python extraction logic, workflow design, process-improvement approach, and portfolio documentation. System-specific SAP field mapping remains a configuration and validation task for the target SAP environment.

## Technology

- Python
- Regular expressions and dataclasses from the standard library
- SAP GUI Scripting adapter interface
- Pytest-based portable unit tests

## Data and safety note

No supplier emails, company workbooks, SAP credentials, or production data are included. Demonstrations should use synthetic or fully redacted data. Authentication and target-system configuration must remain outside source code.
