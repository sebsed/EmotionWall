from flask import Flask, render_template, request, redirect, url_for, jsonify
import base64
from emotion import getEmotion

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Ruta para mandar imagen a analizar
@app.route('/upload', methods=['POST'])
def upload():
    image_data = request.json['image']
    # Codificar imagen en bytes para API de AWS
    image_data = base64.b64decode(image_data.split(',')[1])
    emotion = getEmotion(image_data)
    return jsonify(emotion=emotion)

@app.route('/result')
def result():
    emotion = request.args.get('emotion', '')
    return render_template('result.html', emotion=emotion)

if __name__ == '__main__':
    #app.run()
    app.run(debug=True, host='127.0.0.1', port=5001)
