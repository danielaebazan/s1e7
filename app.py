from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__)

# Definimos la tabla de sistemas averiados
damaged_systems = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

# Variable global para almacenar el sistema averiado actual
damaged_system = None

# Primera llamada: GET /status
@app.route('/status', methods=['GET'])
def get_status():
    global damaged_system
    damaged_system = random.choice(list(damaged_systems.keys()))
    return jsonify({"damaged_system": damaged_system})

# Segunda llamada: GET /repair-bay
@app.route('/repair-bay', methods=['GET'])
def get_repair_bay():
    return render_template('repair_bay.html', code=damaged_systems[damaged_system])

# Tercera llamada: POST /teapot
@app.route('/teapot', methods=['POST'])
def post_teapot():
    global damaged_system
    damaged_system = None
    return '', 418

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)