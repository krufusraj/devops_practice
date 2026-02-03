from flask import Flask, jsonify, request

app = Flask(__name__)

# A simple GET route
@app.route('/', methods=['GET'])
def home():
    return "Welcome to your Flask Backend!"

# A JSON API route
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')
    return jsonify({
        "message": f"Hello, {name}!",
        "status": "success"
    })

if __name__ == '__main__':
    # debug=True automatically reloads the server when you save changes
    app.run(debug=True, port=5000)