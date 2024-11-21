from phi.assistant import Assistant
# from phi.llm.openai import OpenAIChat
from phi.llm.ollama import Ollama
from phi.tools.duckduckgo import DuckDuckGo

assistant = Assistant(
    llm=Ollama(model="smollm2:360m"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
)
assistant.print_response("Search for news from France and write a short poem about it.")
