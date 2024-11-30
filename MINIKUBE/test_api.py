import unittest
import json
from API import app, DATA_FILE

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Limpiar el archivo de datos antes de cada prueba
        with open(DATA_FILE, 'w') as file:
            json.dump([], file)

    def test_get_alumnos(self):
        response = self.app.get('/alumnos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_post_alumno(self):
        new_alumno = {
            "nombre": "Juan",
            "edad": 20,
            "domicilio": "Calle Falsa 123",
            "telefono": "1234567890"
        }
        response = self.app.post('/alumnos', json=new_alumno)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Alumno agregado", response.json["mensaje"])

        response = self.app.get('/alumnos')
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0]["nombre"], "Juan")

    def test_put_alumno(self):
        new_alumno = {
            "nombre": "Juan",
            "edad": 20,
            "domicilio": "Calle Falsa 123",
            "telefono": "1234567890"
        }
        self.app.post('/alumnos', json=new_alumno)

        updated_alumno = {
            "nombre": "Juan",
            "edad": 21,
            "domicilio": "Calle Verdadera 456",
            "telefono": "0987654321"
        }
        response = self.app.put('/alumnos/0', json=updated_alumno)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Alumno actualizado", response.json["mensaje"])

        response = self.app.get('/alumnos/0')
        self.assertEqual(response.json["edad"], 21)

    def test_delete_alumno(self):
        new_alumno = {
            "nombre": "Juan",
            "edad": 20,
            "domicilio": "Calle Falsa 123",
            "telefono": "1234567890"
        }
        self.app.post('/alumnos', json=new_alumno)

        response = self.app.delete('/alumnos/0')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Alumno eliminado", response.json["mensaje"])

        response = self.app.get('/alumnos')
        self.assertEqual(response.json, [])

if __name__ == '__main__':
    unittest.main()
