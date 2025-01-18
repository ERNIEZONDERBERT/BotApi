from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'test'

@app.route("/botcheck/<handle>", methods=['GET'])
def botcheck(handle):
    with open('bots.txt', 'r') as file:
        bots = file.read().splitlines()

    data = {
        'handle': handle,
        'is_bot': handle in bots
    }

    # response = 'bot' if handle in bots else 'not'
    return jsonify(data)
