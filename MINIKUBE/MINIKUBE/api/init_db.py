import sqlite3

def init_db():
    conn = sqlite3.connect('bbdd.db')
    with conn:
        conn.executescript('''
        CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            domicilio TEXT,
            telefono TEXT
        );

        INSERT INTO alumnos (nombre, edad, domicilio, telefono) VALUES
        ('Edson Perez', 22, 'Calle Tec 123', '555-1234'),
        ('Esau Romo', 22, 'Calle Tec 789', '6677889900');
        ''')
    conn.close()

if __name__ == '__main__':
    init_db()
