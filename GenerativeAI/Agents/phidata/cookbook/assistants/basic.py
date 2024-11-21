from phi.assistant import Assistant
# from phi.llm.openai import OpenAIChat
from phi.llm.ollama import Ollama


assistant = Assistant(
    llm=Ollama(model="smollm2:360m"),
    description="You help people with their health and fitness goals.",
    instructions=["Recipes should be under 5 ingredients"],
)
# -*- Print a response to the cli
assistant.print_response("Share a breakfast recipe.", markdown=True)
