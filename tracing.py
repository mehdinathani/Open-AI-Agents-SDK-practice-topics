import os
from pprint import pprint
from typing import Any
from agents import Agent, Runner, Span, Trace, TracingProcessor, set_trace_processors, set_tracing_export_api_key, trace
from agents.tracing.processors import BatchTraceProcessor, default_processor, ConsoleSpanExporter
from agents.tracing.processor_interface import TracingExporter
from dotenv import load_dotenv
from geminiConfig import gemini_config, model
from unittest import result

class CustomConsoleSpanExporter(TracingExporter):
    """Prints the traces and spans to the console."""

    def export(self, items: list[Trace | Span[Any]]) -> None:
        for item in items:
            if isinstance(item, Trace):
                pprint(f"[Exporter] Export trace_id={item.trace_id}, name={item.name}, ")
            elif item.span_data.type == "generation":
                usage = item.span_data.usage or []
                model = item.span_data.model
                user_input = item.span_data.input or []
                agent_output = item.span_data.output or []

                pprint(f"Model used:", model)
                pprint(f"Tokens:", usage)

                if user_input:
                    pprint("User Input:", user_input[-1].get('content', "N/A"))
                if agent_output:
                    pprint("Agent output :", agent_output[0].get('content', "N/A"))

            else:
                pprint(f"[Exporter else] Export span: {item.export()}")


exporter = CustomConsoleSpanExporter()
processor = BatchTraceProcessor(exporter)

load_dotenv()
set_trace_processors([processor,
                      default_processor()
                      ])

api_key = os.getenv("OPENAI_API_KEY")

set_tracing_export_api_key(api_key)

agent = Agent(
    name="CustomAgent",
    instructions="You are a helpful assistant.",
    model=model,
)

async def main():
    with trace("Custom workflow ->"):
        result = await Runner.run(
            starting_agent=agent,
            input="What is agentic AI",
        )

    print(result.final_output)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
