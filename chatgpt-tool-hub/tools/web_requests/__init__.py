"""Tools for making requests to an API endpoint."""
import json
from typing import Any, Dict

from pydantic import BaseModel


def _parse_input(text: str) -> Dict[str, Any]:
    """Parse the json string into a dict."""
    return json.loads(text)


from tools.web_requests.wrapper import RequestsWrapper


class BaseRequestsTool(BaseModel):
    """Base class for requests tools."""

    requests_wrapper: RequestsWrapper


from tools.web_requests.delete import RequestsDeleteTool
from tools.web_requests.get import RequestsGetTool
from tools.web_requests.patch import RequestsPatchTool
from tools.web_requests.post import RequestsPostTool
from tools.web_requests.put import RequestsPutTool


__all__ = (
    "RequestsDeleteTool",
    "RequestsGetTool",
    "RequestsPatchTool",
    "RequestsPostTool",
    "RequestsPutTool"
)