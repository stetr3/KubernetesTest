from flask import Flask, jsonify
import random
app = Flask(__name__)
facts = [
"The Moon has moonquakes.",
"Honey never spoils.",
"A single strand of spider silk is thinner than a human hair, but five times stronger than steel."
]

@app.route('/fact', methods=['GET'])

def get_fact():
    return jsonify({"fact": random.choice(facts)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)