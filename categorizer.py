import ollama
import os

model = "llama3.2"

input_file="./data/grocery_list.txt"
output_file="./data/grocery_list_categorized.txt"

if not os.path.exists(input_file):
    print(f"Input file {input_file} does not exist")
    exit(1)

with open(input_file,"r") as f:
    items = f.read().strip()
    
prompt=f"""
You are an assistant that categorizes and sorts grocery items.

Here is a list of grocery items:
{items}

please:
1. Categorize the items into appopriate categories such vegetables, fruits, dairy, etc.
2. Sort the items in each category alphabetically.
3. Present the categorized list in a clear and organized manner,using bullet points or any other suitable format.
"""

try:
    response=ollama.generate(model=model,prompt=prompt)
    
    generated_text=response.get("response","")
    print(generated_text)
    with open(output_file,"w") as f:
        f.write(generated_text.strip())
        
    print(f"Generated categorized grocery list saved to {output_file}")
    
except Exception as e:
    print(f"Error in generating categorized grocery list: {e}")
    print(response.text)