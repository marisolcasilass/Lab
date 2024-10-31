pipeline {
    agent any
    stages {
        stage('Clonar Repositorio') {
            steps {
                git 'https://github.com/Kristen7770/API-Docker-Py'
            }
        }
        stage('Construir Imagen de Docker') {
            steps {
                script {
                    bat 'docker build -t mi_api_rest .' // Cambiado de sh a bat para Windows
                }
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                script {
                    bat 'docker run mi_api_rest pytest tests/' // Cambiado de sh a bat para Windows
                }
            }
        }
    }
}


