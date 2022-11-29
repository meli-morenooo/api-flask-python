# 💻 API con Flask

## 👥 Integrantes: 
- 🙋🏻‍♂️ Cometto Federico
- 🙋🏻‍♂️ Morales Ciro 
- 🙋🏻‍♀️ Moreno Melisa


## 📝 Descripción del Proyecto

Ejecutar en Docker un proyecto de Python - Flask y subirlo a un repositorio de Github.


## 📦 Guía de uso para Docker 

Se deben ejecutar los siguientes comandos para hacer el build e inicializar la base de datos:

```bash
docker compose build blog
docker compose up db
docker compose run blog bash -c "flask db init && flask db migrate"
```

Una vez completado los pasos anteriores, se debe ejecutar lo siguiente:

```bash
docker compose up -d
docker compose logs -f blog
```

## ❌ Problemas comunes en la ejecución del proyecto

Es posible que en el inicio de docker, se inicialice primero la aplicacion flask y luego la base de datos, por tal motivo en estos casos
se puede ejecutar la app con los siguientes comandos:

```bash
docker compose up -d db
docker compose up -d blog
docker compose logs -f blog
```
