from tools.base_tool import BaseTool
from tools.web_requests import BaseRequestsTool, _parse_input


class RequestsPostTool(BaseRequestsTool, BaseTool):
    """Tool for making a POST request to an API endpoint."""

    name = "requests_post"
    description = """Use this when you want to POST to a website.
    Input should be a json string with two keys: "url" and "data".
    The value of "url" should be a string, and the value of "data" should be a dictionary of 
    key-value pairs you want to POST to the url.
    Be careful to always use double quotes for strings in the json string
    The output will be the text response of the POST request.
    """

    def _run(self, text: str) -> str:
        """Run the tool."""
        try:
            data = _parse_input(text)
            return self.requests_wrapper.post(data["url"], data["data"])
        except Exception as e:
            return repr(e)

    async def _arun(self, text: str) -> str:
        """Run the tool asynchronously."""
        try:
            data = _parse_input(text)
            return await self.requests_wrapper.apost(data["url"], data["data"])
        except Exception as e:
            return repr(e)