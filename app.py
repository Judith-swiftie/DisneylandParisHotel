import csv
import logging
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Configura logging para Render
logging.basicConfig(level=logging.INFO)

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('login.html')

# Ruta para el registro
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    subscribe = data.get('subscribe')
    
    if not email:
        return jsonify({'message': 'No se proporcionó un correo electrónico'}), 400
    
    try:
        with open('datos.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([email, subscribe])
            logging.info(f'Registro guardado: {email}, Suscripción: {subscribe}')  # Registra el dato en logs
    except Exception as e:
        logging.error(f"Error al escribir en datos.csv: {e}")
        return jsonify({'message': 'Error al guardar los datos'}), 500
    
    return jsonify({'message': f'Correo registrado: {email}, Suscripción: {subscribe}'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

