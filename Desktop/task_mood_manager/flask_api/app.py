'''from flask import Flask, request, jsonify

app = Flask(__name__)

MOOD_TIPS = {
    "happy": ["Celebrate with a mini-break!", "Share your joy with a friend."],
    "sad": ["Take a short walk.", "Break tasks into small steps."],
    "tired": ["Try a 15‑minute power nap.", "Switch tasks to stay fresh."],
}

@app.route("/api/tips", methods=["POST"])
def get_tips():
    data = request.get_json() or {}
    mood = data.get("mood", "").lower()
    tips = MOOD_TIPS.get(mood, ["Keep going — you got this!"])
    return jsonify({"tips": tips})

if __name__ == "__main__":
    app.run(port=5001, debug=True)'''

# flask_api/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/tips', methods=['POST'])
def mood_tips():
    data = request.get_json()
    mood = data.get('mood', '').lower()
    tips = {
        'happy': ['Keep the joy!', 'Share your happiness.'],
        'sad':   ['Take a deep breath.', 'Talk to a friend.'],
        'tired': ['Take a short nap.', 'Try a light stretch.']
    }.get(mood, ['Stay positive!', 'Take one step at a time.'])
    return jsonify({'tips': tips})

if __name__ == '__main__':
    app.run(port=5001, debug=True)

