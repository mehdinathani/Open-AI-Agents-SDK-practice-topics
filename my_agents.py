from agents import Agent, Runner, handoff


refund_agent = Agent(
    name="Refund Agent",
    instructions="You are a helpful refund agent. Ask the user what they would like to refund and confirm the refund.",
)

import_shipment_agent = Agent(
    name="Import Shipment Agent",
    instructions="You are a helpful import shipment agent. ask the user about BL number, and then generate invoice for them.",
)

export_shipment_agent = Agent(
    name="Export Shipment Agent",
    instructions="You are a helpful export shipment agent. ask the user about AWB number, and then generate invoice for them.",
)

finance_agent = Agent(
    name="Finance Agent",
    instructions="You are a helpful finance agent. ask the user about invoice number, and advice them how make online payments.",
)


receiption_agent = Agent(
    name="Receiptionist Agent",
    instructions="You are a helpful receiptionist. Greet the user and ask how you can assist them.",
    handoffs=[refund_agent, export_shipment_agent, import_shipment_agent]
)

refund_agent.handoffs.append(receiption_agent)
import_shipment_agent.handoffs.append(receiption_agent)
export_shipment_agent.handoffs.append(receiption_agent)
finance_agent.handoffs.append(receiption_agent)
