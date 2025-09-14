import random
from agents import function_tool

@function_tool
def get_refund_status(bl_number : str) -> str:
    """Get refund status for a given BL number."""
    status = [
        f"Refund status for BL number {bl_number} is pending"
        f"Refund status for BL number {bl_number} is ready"
        f"Refund status for BL number {bl_number} : issue - please call 123-12313 to escalate"
    ]
    return random.choice(status)

@function_tool
def generate_invoice(bl_number : str) -> str:
    """Generate invoice for a given BL number."""
    invoice_number = random.randint(1000, 9999)
    return f"Invoice generated for {bl_number} amount PKR {invoice_number}"

@function_tool
def get_payment_instructions(invoice_number : str) -> str:
    """Get payment instructions for a given invoice number."""
    return f"Please make payment for invoice {invoice_number} using this link: https://example.com/pay/{invoice_number}."

@function_tool
def search_booking_number(query:str) -> str:
    """Search for a booking number."""
    booking_number = random.randint(1000, 9999)
    return f"Your Booking Number is {booking_number}"