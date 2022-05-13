# Django TDD Docker

Test-Driven Development con Django, Django REST framework, y Docker.

## Descripción general de la aplicación

API RESTful desarrollada mediante TDD. La API seguirá los principios del diseño RESTful, utilizando los verbos HTTP:
GET, POST, PUT y DELETE.

| Endpoint        | HTTP method | CRUD method | Result             |
|-----------------|-------------|-------------|--------------------|
| /api/movies     | GET         | READ        | get all movies     |
| /api/movies/:id | GET         | READ        | get a single movie |
| /api/movies     | POST        | CREATE      | add a movie        |
| /api/movies/:id | PUT         | UPDATE      | update a movie     |
| /api/movies/:id | DELETE      | DELETE      | delete a movie     |

## Comandos docker

Construye, (re)crea, inicia contenedores. El flag `-f` indica el archivo docker-compose que se utilizará y `--build`
crea imágenes antes de iniciar contenedores.

```
docker-compose -f docker-compose.yml up --build
```

## Comandos pytest

Normal ejecución

```
docker-compose exec movies pytest
```

Deshabilitar warnings

```
docker-compose exec movies pytest -p no:warnings
```

Ejecutar solo las últimas pruebas fallidas

```
docker-compose exec movies pytest --lf
```

Ejecutar solo las pruebas con nombres que coincidan con la expresión de caden

```
docker-compose exec movies pytest -k "movie and not all_movies"
```

Detener la sesión de prueba después del primer fallo

```
docker-compose exec movies pytest -x
```

Ingrese PDB después del primer error y luego finalice la sesión de prueba

```
docker-compose exec movies pytest -x --pdb
```

Detener la ejecución de la prueba después de dos fallas

```
docker-compose exec movies pytest --maxfail=2
```

Mostrar variables locales en rastreos

```
docker-compose exec movies pytest -l
```

Enumerar las 2 pruebas más lentas

```
docker-compose exec movies pytest --durations=2
```
