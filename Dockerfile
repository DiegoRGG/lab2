# Dockerfile

# ¡CAMBIO AQUÍ! Usaremos una versión específica de TensorFlow
# tensorflow/tensorflow:2.15.0 es una buena opción estable
FROM tensorflow/tensorflow:2.15.0

WORKDIR /app

# Copia el archivo de requisitos al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias de Python desde requirements.txt
# Quitamos --break-system-packages por ahora, ya que podría no ser necesario en esta versión de la imagen base.
# Si el error persiste con esta nueva base, podemos considerar reintroducirlo o investigar más a fondo.
RUN pip install --no-cache-dir -r requirements.txt

# Copia tu aplicación Flask/FastAPI (ej. app.py) al directorio de trabajo
COPY app.py .

# Expone el puerto que tu aplicación Flask/FastAPI usará
EXPOSE 5000

# Comando para ejecutar tu aplicación cuando se inicie el contenedor
CMD ["python", "app.py"]