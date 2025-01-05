import ollama

# response = ollama.list()

# print(response)

# res = ollama.chat(
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

# print(res["message"]["content"])

# res = ollama.generate(
#     model="llama3.2",
#     prompt="tell me a short story and make it funny"
# )

# print(ollama.show("llama3.2"))

modlefile="""
FROM llama3.2
PARAMETER temperature 1
SYSTEM You are james, a very smart assistant who answers questions succintly and informatively
"""

ollama.create(model="james",modelfile=modlefile)

res=ollama.generate(model="james",prompt="what is the capital of france")

print(res)


ollama.delete("james")