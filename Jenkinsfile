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
                    bat 'docker build -t mi_api_rest .'
                }
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                script {
                    bat 'docker run --rm mi_api_rest python -m pytest tests/'
                }
            }
        }
    }
}
