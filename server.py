from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests for development purposes

@app.route('/generate', methods=['POST'])
def generate():
    # Retrieve data from the request
    data = request.json
    timeframe = data.get('timeframe')
    calorie_goal = data.get('calorieGoal')

    # Process the data and return some dummy recipes
    query = f"""
    Generate a high protein meal prep plan with the following details
    timeframe:{timeframe}
    calorie goal: {calorie_goal}
    """
    answer = generate_llm_response(query=query)
    response = {
        "timeframe": timeframe,
        "calorieGoal": calorie_goal,
        "recipe": answer
    }
    return jsonify(response)

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

client = OpenAI(
    api_key=load_json_key("openai_api.json","key"),  # This is the default and can be omitted
)

def generate_llm_response(query):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": query,
        }
    ],
    model="gpt-4o",
    )
    answer = chat_completion.choices[0].message.content
    return answer

if __name__ == '__main__':
    app.run(debug=True)
