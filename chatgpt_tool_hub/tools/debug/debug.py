from typing import Callable

from pydantic import Field

from chatgpt_tool_hub.tools.all_tool_list import register_tool
from chatgpt_tool_hub.tools.base_tool import BaseTool

default_tool_name = "debug"


def _print_func(text: str) -> None:
    print("\n")
    print(text)


class DebugTool(BaseTool):
    """Tool for asking for help."""

    name = default_tool_name
    description = (
        "You can ask a helper for guidance when you think you "
        "got stuck or you are not sure what to do next. "
        "The input should be a question for the human in chinese."
    )
    prompt_func: Callable[[str], None] = Field(default_factory=lambda: _print_func)
    input_func: Callable = Field(default_factory=lambda: input)

    def _run(self, query: str) -> str:
        """Use the DebugTool tool."""
        self.prompt_func(query)
        return self.input_func()

    async def _arun(self, query: str) -> str:
        """Use the DebugTool asynchronously."""
        raise NotImplementedError("DebugTool does not support async")


register_tool(default_tool_name, lambda _: DebugTool(), [])