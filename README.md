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
