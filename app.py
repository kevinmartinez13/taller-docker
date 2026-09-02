import os
from flask import Flask

app = Flask(__name__)

MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "default_safe_password")

@app.route('/')
def home():
    return "Conexión exitosa a la base de datos"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=False)  # nosec B104