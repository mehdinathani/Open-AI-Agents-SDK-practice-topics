from typing import Any, Optional
from agents import Agent, ModelResponse, RunContextWrapper, RunHooks, TResponseInputItem, Tool


class myrunhooks(RunHooks):
    async def on_llm_start(
        self,
        context: RunContextWrapper,
        agent: Agent,
        system_prompt: Optional[str],
        input_items: list[TResponseInputItem],
    ) -> None:
        """Called just before invoking the LLM for this agent."""
        print("""Called just before invoking the LLM for this agent.""")

    async def on_llm_end(
        self,
        context: RunContextWrapper,
        agent: Agent,
        response: ModelResponse,
    ) -> None:
        """Called immediately after the LLM call returns for this agent."""
        print("""Called immediately after the LLM call returns for this agent.""")

    async def on_agent_start(self, context: RunContextWrapper, agent: Agent) -> None:
        """Called before the agent is invoked. Called each time the current agent changes."""
        print("""Called before the agent is invoked. Called each time the current agent changes.""")

    async def on_agent_end(
        self,
        context: RunContextWrapper,
        agent: Agent,
        output: Any,
    ) -> None:
        """Called when the agent produces a final output."""
        print("""Called when the agent produces a final output.""")

    async def on_handoff(
        self,
        context: RunContextWrapper,
        from_agent: Agent,
        to_agent: Agent,
    ) -> None:
        """Called when a handoff occurs."""
        print("""Called when a handoff occurs.""")

    async def on_tool_start(
        self,
        context: RunContextWrapper,
        agent: Agent,
        tool: Tool,
    ) -> None:
        """Called concurrently with tool invocation."""
        print("""Called concurrently with tool invocation.""")

    async def on_tool_end(
        self,
        context: RunContextWrapper,
        agent: Agent,
        tool: Tool,
        result: str,
    ) -> None:
        """Called after a tool is invoked."""
        print("""Called after a tool is invoked.""")
