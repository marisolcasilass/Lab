from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Lista para almacenar los datos de los alumnos
alumnos = []

# Definimos el recurso Alumno
class Alumno(Resource):
    def get(self):
        """Obtiene la lista de alumnos."""
        return jsonify(alumnos)

    def post(self):
        """Agrega un nuevo alumno."""
        data = request.get_json()
        alumno = {
            "nombre": data.get("nombre"),
            "edad": data.get("edad"),
            "domicilio": data.get("domicilio"),
            "telefono": data.get("telefono")
        }
        alumnos.append(alumno)
        return jsonify({"mensaje": "Alumno agregado", "alumno": alumno})

# Definimos el recurso para un alumno específico por índice
class AlumnoEspecifico(Resource):
    def get(self, alumno_id):
        """Obtiene un alumno por su ID."""
        if 0 <= alumno_id < len(alumnos):
            return jsonify(alumnos[alumno_id])
        return jsonify({"mensaje": "Alumno no encontrado"}), 404

    def put(self, alumno_id):
        """Actualiza la información de un alumno específico."""
        if 0 <= alumno_id < len(alumnos):
            data = request.get_json()
            alumno = alumnos[alumno_id]
            alumno.update({
                "nombre": data.get("nombre", alumno["nombre"]),
                "edad": data.get("edad", alumno["edad"]),
                "domicilio": data.get("domicilio", alumno["domicilio"]),
                "telefono": data.get("telefono", alumno["telefono"])
            })
            return jsonify({"mensaje": "Alumno actualizado", "alumno": alumno})
        return jsonify({"mensaje": "Alumno no encontrado"}), 404

    def delete(self, alumno_id):
        """Elimina un alumno por su ID."""
        if 0 <= alumno_id < len(alumnos):
            eliminado = alumnos.pop(alumno_id)
            return jsonify({"mensaje": "Alumno eliminado", "alumno": eliminado})
        return jsonify({"mensaje": "Alumno no encontrado"}), 404

# Agregamos las rutas para los recursos
api.add_resource(Alumno, '/alumnos')
api.add_resource(AlumnoEspecifico, '/alumnos/<int:alumno_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)