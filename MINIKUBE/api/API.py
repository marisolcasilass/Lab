from flask import Flask, request, jsonify
from database import get_db_connection
import sqlite3
import os


app = Flask(__name__)


def get_db_connection():
    db_path = "/mnt/data/sqlite/datab.db"
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

# Ruta para obtener todos los alumnos
@app.route('/alumnos', methods=['GET'])
def get_alumnos():
    conn = get_db_connection()
    alumnos = conn.execute('SELECT * FROM alumnos').fetchall()
    conn.close()
    return jsonify([dict(alumno) for alumno in alumnos])

# Ruta para agregar un alumno
@app.route('/alumnos', methods=['POST'])
def add_alumno():
    data = request.get_json()
    nombre = data.get('nombre')
    edad = data.get('edad')
    domicilio = data.get('domicilio', '')
    telefono = data.get('telefono', '')

    if not nombre or not edad:
        return jsonify({'error': 'Faltan campos obligatorios'}), 400

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO alumnos (nombre, edad, domicilio, telefono) VALUES (?, ?, ?, ?)',
        (nombre, edad, domicilio, telefono)
    )
    conn.commit()
    conn.close()
    return jsonify({'message': 'Alumno agregado con éxito'}), 201

# Ruta para obtener un alumno por ID
@app.route('/alumnos/<int:id>', methods=['GET'])
def get_alumno(id):
    conn = get_db_connection()
    alumno = conn.execute('SELECT * FROM alumnos WHERE id = ?', (id,)).fetchone()
    conn.close()

    if alumno is None:
        return jsonify({'error': 'Alumno no encontrado'}), 404

    return jsonify(dict(alumno))

# Ruta para eliminar un alumno por ID
@app.route('/alumnos/<int:id>', methods=['DELETE'])
def delete_alumno(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM alumnos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Alumno eliminado con éxito'}), 200

# Ruta para actualizar los datos de un alumno por ID
@app.route('/alumnos/<int:id>', methods=['PUT'])
def update_alumno(id):
    data = request.get_json()
    nombre = data.get('nombre')
    edad = data.get('edad')
    domicilio = data.get('domicilio', '')
    telefono = data.get('telefono', '')

    conn = get_db_connection()
    conn.execute(
        'UPDATE alumnos SET nombre = ?, edad = ?, domicilio = ?, telefono = ? WHERE id = ?',
        (nombre, edad, domicilio, telefono, id)
    )
    conn.commit()
    conn.close()
    return jsonify({'message': 'Alumno actualizado con éxito'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)