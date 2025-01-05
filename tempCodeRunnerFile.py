res = ollama.chat(
#     model="llama3.2",
#     messages=[
#         {
#             "role": "user",
#             "content": "tell me a short story and make it funny"
#         }
#     ],
#     stream=True
# )

# for chunk in res:
#     print(chunk["message"]["content"],end="",flush=True)