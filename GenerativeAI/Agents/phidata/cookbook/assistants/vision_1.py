from phi.assistant import Assistant
from phi.llm.ollama import Ollama

# Initialize the Assistant
assistant = Assistant(llm=Ollama(model="llava-phi3:latest"))

# Construct the message
message = (
    "Compare the following two images and describe any differences between them in one sentence:\n"
    "1. Image URL: https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg\n"
    "2. Image URL: data:image/jpeg;base64,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"
)

# Call the assistant
response = assistant.print_response(message, markdown=True)
print(response)
