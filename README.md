### Capturas contenedor y archivo jenkinsfile

- Api REST

# Instrucciones:

- Crear una API REST



- Conteneriza tu aplicacion (con Docker)

![ice_screenshot_20241031-222141](https://github.com/user-attachments/assets/97945544-209a-430a-8664-548395ba00d6)


Debido a que no contamos con sistema operativo linux los comando de `run_docker.sh` tuvieron que ser ejecutados directamente en el shell de windows. 

####Comandos para el shell　

```javascript
docker build -t apirest-running .

docker run -p 5000:5000 apirest-running
```


![ice_screenshot_20241031-222802](https://github.com/user-attachments/assets/4045cfe0-9d8a-4daa-bca1-845521c941ac)

![ice_screenshot_20241031-222834](https://github.com/user-attachments/assets/4367c927-518f-4e2f-a69b-fe12d2792431)


Resultado: 
![WhatsApp Image 2024-10-31 at 10 07 07 PM](https://github.com/user-attachments/assets/704f1517-9947-42c5-bb77-dd2b77025b99)

- Realiza una prueba de tu API REST utilizando jenkins.

![WhatsApp Image 2024-10-31 at 10 09 45 PM](https://github.com/user-attachments/assets/5c2c1426-ce54-43cf-9dbd-6b491ad98d75)


- Mostrar el codigo para las pruebas

![WhatsApp Image 2024-10-31 at 10 07 24 PM](https://github.com/user-attachments/assets/861611cf-0138-445e-9106-9a56ee1fe306)

![WhatsApp Image 2024-10-31 at 10 09 04 PM](https://github.com/user-attachments/assets/681dac3a-f845-4413-aa00-6998c3f61380)

LISTA CORRIENDO LA API
![a8057adc-9d7f-4e54-b066-7ce363833ac7](https://github.com/user-attachments/assets/6ee11359-6213-419e-ad05-e98c31173ae9)

POR ID
![90f229fd-77e3-4053-ac20-4794738409f4](https://github.com/user-attachments/assets/75cf5f7d-e8e5-4fdf-a5ae-62c1c09c3ad3)

INSERT DE USUARIO
![c2debaf1-e7d7-4048-91e9-15fc170cd82e](https://github.com/user-attachments/assets/8aa7ae3d-68fd-47f4-a247-b76977680030)

ACTUALIZAR
![3e624561-0800-432f-82a4-76fb24359987](https://github.com/user-attachments/assets/91dec1c8-10f3-4e9a-8385-e5ac23997cca)

ELIMINAR
![61025841-c002-445f-94a2-ef539fe7c862](https://github.com/user-attachments/assets/a02fb314-7ee6-4d22-8480-89715183197b)







