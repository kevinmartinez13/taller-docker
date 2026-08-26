from flask import Flask

app = Flask(__name__)

# Fallo de SAST (Bandit): Clave sensible quemada en texto plano
MYSQL_PASSWORD = "super_secret_123"

@app.route('/')
def home():
    return "Conexión exitosa a la base de datos"

if __name__ == '__main__':
    # Fallo de SAST (Bandit): Modo depuración activado en producción
    app.run(host='0.0.0.0', port=5050, debug=True)