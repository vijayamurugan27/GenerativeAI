from phi.assistant import Assistant
from phi.llm.ollama import Ollama

assistant = Assistant(
    llm=Ollama(model="smollm2:360m"),
    system_prompt="Share a 2 sentence story about",
    debug_mode=True,
)
assistant.print_response("Love in the year 12000.")
