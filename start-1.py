import requests
import json

url = "http://localhost:11434/api/generate"

data ={
    "model":"llama3.2",
    "prompt":"tell me a short story and make it funny"
}

response = requests.post(url, json=data,stream=True)

#Check if the response is successful
if response.status_code == 200:
    for line in response.iter_lines():
        if line:
            decoded_line=line.decode('utf-8')
            result=json.loads(decoded_line)
            generate_text=result.get("response","")
            print(generate_text,end="",flush=True)
else:
    print("Error in response")
    print(response.text)
    
    
    



