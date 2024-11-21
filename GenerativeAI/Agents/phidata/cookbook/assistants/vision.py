from phi.assistant import Assistant
# from phi.llm.openai import OpenAIChat
from phi.llm.ollama import Ollama

assistant = Assistant(llm=Ollama(model="llava-phi3:latest"))

# # Single Image
# assistant.print_response(
#     [
#         {"type": "text", "text": "What's in this image, describe in 1 sentence"},
#         {
#             "type": "image_url",
#             "image_url": {
#                 "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
#             },
#         },
#     ]
# )



# # Multiple Images
# assistant.print_response(
#     [
#         {
#             "type": "text",
#             "text": "Is there any difference between these. Describe them in 1 sentence.",
#         },
#         {
#             "type": "image_url",
#             "image_url": {
#                 "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
#             },
#         },
#         {
#             "type": "image_url",
#             "image_url": {
#                 "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
#             },
#         },
#     ],
#     markdown=True,
# )


message = (
    "Please analyze the image available at the URL below and describe its content in one sentence: "
    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
)

# Call the assistant to generate a response
response = assistant.print_response(message)
print(response)