from phi.assistant import Assistant
# from phi.llm.openai import OpenAIChat
from phi.llm.ollama import Ollama

assistant = Assistant(
    llm=Ollama(model="smollm2:135m"),
    description="You are a rocket scientist",
)
assistant.print_response("write a plan to go to the moon stp by step", markdown=True)
