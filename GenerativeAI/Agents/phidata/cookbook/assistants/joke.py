from phi.assistant import Assistant
# from phi.llm.openai import OpenAIChat
from phi.llm.ollama import Ollama

topic = "ice cream"
assistant = Assistant(llm=Ollama(model="tinyllama:latest"))
assistant.print_response(f"Tell me a joke about {topic}")
