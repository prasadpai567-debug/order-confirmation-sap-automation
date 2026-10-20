"""SAP GUI Scripting adapter for order-confirmation entry."""

class SapGuiAdapter:
    def __init__(self, session):
        self.session = session

    def enter_confirmation(self, confirmation) -> None:
        # Replace placeholders with SAP field IDs for your system.
        raise NotImplementedError("Configure SAP GUI field selectors for your system.")

    def attach_source_email(self, email_path: str) -> None:
        raise NotImplementedError("Configure SAP attachment handling for your system.")
