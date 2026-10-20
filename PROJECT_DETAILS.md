# Order Confirmation Entries in SAP

## Business problem
Order confirmations were previously entered manually in SAP. The process required searching emails, extracting the acknowledgement number, delivery date, price, and delivery address, and attaching the source email.

## Solution
A Python desktop automation workflow extracts the required details, validates them, enters them into SAP through SAP GUI Scripting, and attaches the original email to the SAP record.

## Results
- Processing time reduced from approximately 3–5 minutes to 20–30 seconds per confirmation.
- Approximately 95% accuracy based on reported workflow results.
- Repetitive manual entry significantly reduced.
- Better traceability through source-email attachment.

## Contribution
I identified the improvement opportunity and completed the Python logic, workflow design, process improvement, and application development.

## Technology
Python · SAP GUI Scripting · Tkinter · Excel automation · Windows automation

## Note
This repository is a reconstructed portfolio implementation based on the packaged application and documented workflow. SAP field IDs, transaction details, and email patterns must be configured for the target SAP system.
