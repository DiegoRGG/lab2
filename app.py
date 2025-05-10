# app.py (tu script de Flask)
from flask import Flask, request, jsonify
import cv2
from mtcnn.mtcnn import MTCNN
import numpy as np # Para manejar la imagen de entrada como array

app = Flask(__name__)
detector = MTCNN() # Cargar tu modelo una vez

@app.route('/detect_faces', methods=['POST'])
def detect_faces_api():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files['image'].read()
    npimg = np.fromstring(file, np.uint8)
    image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    if image is None:
        return jsonify({"error": "Could not decode image"}), 400

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = detector.detect_faces(image_rgb)

    # Formatear los resultados para la respuesta JSON
    formatted_results = []
    for face in results:
        formatted_results.append({
            "box": face['box'],
            "confidence": float(face['confidence']), # Convertir a float para JSON
            "keypoints": {k: [int(v[0]), int(v[1])] for k, v in face['keypoints'].items()}
        })

    return jsonify(formatted_results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)