from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables cross-origin requests from the Express frontend

@app.route('/')
def home():
    return "This is Home"

@app.route('/api/submit', methods=['POST'])
def handle_submit():
    data = request.json
    username = data.get('username', 'Anonymous')
    email = data.get('email', 'Not provided')
    
    # Simulating data handling/response
    return jsonify({
        "status": "success",
        "message": f"Data received for {username} ({email}) on the Flask backend!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
