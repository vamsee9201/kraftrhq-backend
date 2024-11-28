from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests for development purposes

@app.route('/generate', methods=['POST'])
def generate():
    # Retrieve data from the request
    data = request.json
    timeframe = data.get('timeframe')
    calorie_goal = data.get('calorieGoal')

    # Process the data and return some dummy recipes
    response = {
        "recipes": [
            {"name": "Grilled Chicken Salad", "calories": 300},
            {"name": "Quinoa Bowl", "calories": 350},
        ],
        "timeframe": timeframe,
        "calorieGoal": calorie_goal,
    }
    return jsonify(response)

def generate_llm_response(query):
    answer = ""
    return answer

if __name__ == '__main__':
    app.run(debug=True)
