# Contenizar una aplicación Python con Docker + Kubernetes local

![Python + Docker](/img/Python+Docker.jpg)

## Introducción

Esta sección explicará como desplegar un contenedor de una app Python en un kubernetes en ambiente local usando el WSL2.

## Que vamos hacer en este laboratorio?

1. Obtener un código fuente escrito en python y ejecutarlo en local
2. Crear una imagen docker y luego ejecutarla
3. Adecuar el ambiente local de Kubernetes con algún servicio que permita gestionar clúster local, en este caso vamos a usar WSL2
### Nota: 
Kubernetes solo corre nativamente en distribuciones Linux.

## Contenido

* Conceptos generales de virtualización
* Pre-requisitos necesarios para llevar acabo el laboratorio
* Preparación de la imagen docker de Python
* Implementación de la imagen docker
* Ejecución en Kubernetes
* Glosario

### Conceptos generales de virtualización:

#### ¿Que es Docker?

![Docker](/img/Docker.jpg)

Docker es una solución open source usada para virtualizar ambientes de ejecución para que cualquier aplicación puede correr en cualquier sistemas operativo.

#### ¿Que es Kubernetes?

![K8s](/img/K8s.jpg)

Kubernetes (tambien conocido como K8s) es una solución open source usada para orquestar contenedores, esto quiere decir que su objetivo es automatizar la implementación, el escalado y la administración de aplicaciones en contenedores.

#### ¿Que es Kind?

![Kind](/img/Kind.jpg)

kind es una herramienta para ejecutar clústeres de Kubernetes locales mediante los "nodos" de contenedor de Docker.
kind fue diseñado principalmente para probar el propio Kubernetes, pero puede usarse para desarrollo local o CI.

#### ¿Que es minikube?

![minikube](/img/minikube.jpg)

minikube es Kubernetes local y se centra en facilitar el aprendizaje y el desarrollo para Kubernetes. Todo lo que necesita es un contenedor Docker (o similarmente compatible) o un entorno de máquina virtual.

#### ¿Que es WSL2?

![wsl](/img/wsl.jpg)

WSL es el acrónimo de Windows Subsystem for Linux, es una capa de compatilidad desarrollada por Microsoft que permite correr una distribución Linux nativamente sobre una consola shell en el Sistema operativo Windows 10(Tambien corre en Windows Server 2019).

### Pre-requisitos necesarios para llevar acabo el laboratorio:

* SO: Windows 10 versión 2004, compilación 19041, con Distribución WSL2 habilitado.
    Links de referencia:
    https://docs.microsoft.com/en-us/windows/wsl/install-win10
    https://docs.docker.com/docker-for-windows/wsl/
    https://pandorafms.com/blog/es/wsl2/
* Docker Desktop
* [Opcional] Microsoft Terminal instalado desde la Tienda Windows 
* Un servicio de Kubernetes local, como Kind y/o minikube.
    Link de referencia:
    https://kubernetes.io/blog/2020/05/21/wsl-docker-kubernetes-on-the-windows-desktop/
* Python 3.8 instalado

### Preparación de la imagen docker de Python:

Lo primero que vamos hacer es ejecutar localmente la app Python para asegurarnos que este correcta.

```
pip install -r requirements.txt
python main.py
```

Luego vamos a crear el archivo Dockerfile
```
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
```
Dockerfile es un conjunto de instrucciones que Docker utilizará para crear la imagen. Para esta sencilla aplicación, Docker va a:

1. Obtenga la imagen base oficial de Python para la versión 3.7 de Docker Hub.
2. En la imagen, cree un directorio llamado app.
3. Establezca el directorio de trabajo en ese nuevo directorio de aplicaciones.
4. Copie el contenido del directorio local a esa nueva carpeta en la imagen.
5. Ejecute el instalador de pip (como hicimos antes) para incorporar los requisitos a la imagen.
6. Informe a Docker que el contenedor escucha en el puerto 5000.
7. Configure el comando de inicio que se utilizará cuando se inicie el contenedor.

Luego vamos a crear una imagen docker apartir de las instrucciones dadas en el archivo Dockerfile

```
docker build . -t python-docker:latest
```

es recomendable listar las imagenes de Docker para validar que se haya creado correctamente:

```
docker image ls
```
La aplicación ahora está en contenedores, lo que significa que ahora se puede ejecutar en Docker y Kubernetes.

#### Fuente de consulta:
https://docs.docker.com/language/python/build-images/

### Implementación de la imagen Docker:

Antes de saltar a Kubernetes, verifiquemos que funciona en Docker. Ejecute el siguiente comando para que Docker ejecute la aplicación en un contenedor.
```
docker run -p 5001:5000 python-docker
```
Luego ejecute el siguiente comando y debería de correr la app correctamente.
```
curl http: // localhost: 5001
```

### Ejecución en Kubernetes:
Primero verifique que su kubectl esté configurado. En la línea de comando, escriba lo siguiente:
```
kubectl version
```
¡Ahora está trabajando con Kubernetes! Puede ver el nodo escribiendo:
```
kubectl get nodes
```
Ahora hagamos que ejecute la aplicación. Cree un archivo llamado deployment.yaml y agréguele el siguiente contenido y luego guárdelo:
```
apiVersion: v1
kind: Service
metadata:
  name: python-docker-service
spec:
  selector:
    app: python-docker
  ports:
  - protocol: "TCP"
    port: 6000
    targetPort: 5000
  type: LoadBalancer

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-docker
spec:
  selector:
    matchLabels:
      app: python-docker
  replicas: 4
  template:
    metadata:
      labels:
        app: python-docker
    spec:
      containers:
      - name: python-docker
        image: python-docker
        imagePullPolicy: Never
        ports:
        - containerPort: 5000
```
Este archivo YAML son las instrucciones para Kubernetes sobre lo que desea ejecutar. Le dice a Kubernetes lo siguiente:

* Quiere un servicio de carga balanceada que exponga el puerto 6000
* Quieres cuatro instancias del contenedor python-docker ejecutándose

Use kubectl para enviar el archivo YAML a Kubernetes ejecutando el siguiente comando:
```
kubectl apply -f deployment.yaml
```
Puede ver que los pods se están ejecutando si ejecuta el siguiente comando:
```
kubectl get pods
```

### Glosario:

#### Contenedor: 
Es la virtualización de entorno de tiempo de ejecución en cual tiene todo lo necesario para que una aplicación pueda correr.
#### Virtualización: 
Es la creación de un subsistema que emula digiatalmente un recurso.
#### Máquina virtual: 
Es un software que simula un sistema informatico.
#### Orquestador: 
Es un software que permite la agrupación e integración de componentes de unidades lógicas para su gestión y darles visibilidad.
#### Subsistema:
Es un sistema que se ejecuta sobre otro sistema que lo contiene. 
#### Consola shell:
Es una terminal en que corre un programa que tiene como objetivo procesar comandos para interactuar con el sistema operativo y gestionar procesos en primer y segundo plano.