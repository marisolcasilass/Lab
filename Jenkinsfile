pipeline {
    agent any
    stages {
        stage('Clonar Repositorio') {
            steps {
                git url: 'https://github.com/marisolcasilass/Lab'
            }
        }
        stage('Construir Imagen de Docker') {
            steps {
                script {
                    // Construir la imagen Docker sin caché
                    bat 'docker build --no-cache -t mi_api_rest .'
                }
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                script {
                    // Ejecutar pytest en el contenedor
                    bat 'docker run --rm mi_api_rest python -m pytest tests/'
                }
            }
        }
    }
}

