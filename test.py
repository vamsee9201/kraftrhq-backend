#%%
import json
import os
from openai import OpenAI
#%%
# Load JSON from a file
def load_json_key(file_path, key):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            # Access the desired key
            return data.get(key, f"Key '{key}' not found")
    except FileNotFoundError:
        return "File not found."
    except json.JSONDecodeError:
        return "Error decoding JSON."
#%%
client = OpenAI(
    api_key=load_json_key("openai_api.json","key"),  # This is the default and can be omitted
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "who is the president of united states",
        }
    ],
    model="gpt-4o",
)

# %%
print(chat_completion.choices[0].message.content)
# %%
