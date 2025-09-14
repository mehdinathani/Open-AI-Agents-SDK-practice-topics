from agents import Agent, Runner, handoff
from my_tools import get_refund_status, generate_invoice, get_payment_instructions, search_booking_number


refund_agent = Agent(
    name="Refund Agent",
    instructions="""You are the helpful refund agent. 
    ask for the BL number to check refund status using get_refund_status tool. 
    if the status requires escalation, offer to transfer to the receptionist. 
    Confirm the refund status with the user""",
    tools=[get_refund_status]
)

import_shipment_agent = Agent(
    name="Import Shipment Agent",
    instructions="""You are a helpful import shipment agent. 
    ask the user about BL number, and then generate invoice for them usng generate_invoice tool.
    and offer to transfer to finance for payment or receiption for further quries""",
    tools=[generate_invoice,get_payment_instructions, search_booking_number]
)

export_shipment_agent = Agent(
    name="Export Shipment Agent",
    instructions="""You are a helpful export shipment agent. 
    ask the user about AWB number, and then generate invoice for them.
    and offer to transfer to finance for payment or receiption for further quries""",
    tools=[generate_invoice,get_payment_instructions, search_booking_number]
)

finance_agent = Agent(
    name="Finance Agent",
    instructions="""You are a helpful finance agent. 
    Ask for the invoice number and provide payment instructions using get_payment_instructions. 
    If the user needs other help, offer to transfer to the receptionist.""",
    tools=[get_payment_instructions]
)


reception_agent = Agent(
    name="Receptionist Agent",
    instructions="""You are helful receptionist, greet the user with Welcome to ABC shipping pvt. ltd.
    identify their quries, for refunds, handoffs to refund agent, For shipments handoffs to export or import shipment agents as per user query
    for payment related queries handoffs to finance agent.
    for general quries use search booking number and handoff to export or import shipment""",
    handoffs=[refund_agent, export_shipment_agent, import_shipment_agent],
    tools=[search_booking_number]
)

refund_agent.handoffs.append(reception_agent)
import_shipment_agent.handoffs.append(reception_agent)
export_shipment_agent.handoffs.append(reception_agent)
finance_agent.handoffs.append(reception_agent)
