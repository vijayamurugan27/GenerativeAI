from phi.llm.ollama import Ollama
from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo

assistant = Assistant(
    llm=Ollama(model="llama3.2:1b"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    read_chat_history=True,
    debug_mode=True,
    add_chat_history_to_messages=True,
    num_history_messages=3,

)
assistant.cli_app(markdown=True)
