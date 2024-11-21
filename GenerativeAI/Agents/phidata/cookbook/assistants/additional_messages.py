from phi.assistant import Assistant
# from phi.llm.openai import OpenAIChat
from phi.llm.ollama import Ollama


Assistant(
    llm=Ollama(model="smollm2:360m", stop="</answer>"),
    system_prompt="What is the color of a banana? Provide your answer in the xml tag <answer>.",
    additional_messages=[{"role": "assistant", "content": "<answer>"}],
    debug_mode=True,
).print_response()
