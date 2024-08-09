# Event-Management-Api

The Event Management RESTful API is a server-side application that allows users to manage events. It provides endpoints for different access levels, allowing users to view events and administrators to manage them. Users can register for events, and administrators can add, remove, or edit events. The API supports search functionality, allowing users to search for events by title, date, or location.

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54&label=3.12) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white) ![Alembic](https://img.shields.io/badge/Alembic-091132?style=for-the-badge&logo=alembic&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white) ![Pipenv](https://img.shields.io/badge/Pipenv-557C9B?style=for-the-badge&logo=pipenv&logoColor=white)

---

## API Documentation

* [Swagger API Documentation](https://event-management-api-o6iz.onrender.com/docs)

### Repository Link

* [Github](https://github.com/nileshverma054/event-management-api)

### Authentication and Authorization

* The API uses JSON Web Tokens (JWT) for authentication.
* The API supports two types of users: admin and regular users.
* The API uses the following roles:`user`
  * `admin`: The user is an administrator. An administrator can add, remove, or edit events.
  * `user`: The user is a regular user. A regular user can view events and register for them. In order to register for an event the user must signup first.
* The API uses the following algorithms to sign the JWT:
  * `HS256`: A secret key is used to sign and verify the JWT.
* The API uses the following headers to verify the JWT:
  * `Authorization`: The JWT is passed in the `Authorization` header: `Authorization: Bearer <token>`

---

### TODO

* [x] Project Setup
* [x] API Documentation
* [x] Database Migration with Alembic
* [x] Use pipenv to manage dependencies
* [x] Events API
  * [x] Add events
  * [x] Get events
  * [x] Edit events
  * [x] Remove events
  * [x] Register for events
  * [x] Search functionality for events
* [x] Authentication
* [x] Authorization
* [x] Deployment
* [x] Databse rollback support
* [ ] Containerization with Docker and Docker Compose
* [ ] Tests for the API
* [ ] Add SAML support

## Project Setup

### Install dependencies

Below command will create a virtual env and install all dependencies from pipenv.lock

```shell
pipenv install
```

### Database Migration

* Initialise the database migration

```bash
 alembic init migrations
```

* Create a new migration

```bash
 alembic revision --autogenerate -m "commit message"
```

* Apply migration

```bash
 alembic upgrade head
```

* Seed Database

```bash
 python scripts/manage.py seed-db
```

* Create User

```bash
 python scripts/manage.py create-user <first_name> <last_name> <email> <role>
```

* CLI Help

```bash
 python scripts/manage.py -h
```

### Run App

```bash
 fastapi dev
```

---

### Why Pipenv?

Pipenv is a tool that helps you manage your Python project dependencies. It provides a clean and reproducible development environment that is easy to use.

* Seperate development and production dependencies
  * To install dependencies on prod run `pipenv install --ignore-pipfile` which will install all dependencies from Pipfile.lock leading to deterministic build.
  * To install dependencies on dev run `pipenv install --dev` which will install both regular and dev dependencies.
* Specify Python version in Pipfile
* Auto-update dependencies in Pipefile when package is installed or uninstalled
* Easy virtualenv management

#### Pipenv useful commands

* Create virtual environment with specific python version

```shell
 pipenv shell --python 3.12
```

* Activate virtual environment

```shell
 pipenv shell
```

* Deactivate virtual environment

```shell
 exit
```

* Install dependencies from Pipfile. This will also create virtual environment if does not exist.

```shell
 pipenv install
```

* Install a dev dependent package

```shell
 pipenv install pytest --dev
```

* Run command without activating virtual environment
*eg. pipenv run fastapi dev*

```shell
pipenv run <command> 
```

* Check security vulnerabilities

```shell
pipenv check
```

* Migrate to pipenv - this will install dependencies from requirement.txt

```shell
pipenv install
```

---

## Requirement Details for reference

### Event Management RESTful API

**Objective**: Create a RESTful API for managing events.
The API should support different access levels, allowing users to view events and administrators to manage them.

**Requirements**:

* Framework and Database: Use FastAPI for the framework. Use a database of your choice (e.g., PostgreSQL, MySQL, MongoDB).

* Access Levels:
  * Admin: Can add, remove, or edit events.
  * Users: Can view events and register for them.
* API Endpoints:
  * Admin Endpoints (Require authentication):
        POST /events: Add a new event.
        PUT /events/{event_id}: Edit an existing event.
        DELETE /events/{event_id}: Delete an event.
  * User Endpoints:
    * GET /events: View all events.
    * GET /events/{event_id}: View a specific event.
    * POST /events/{event_id}/register: Register for an event.
            Search Functionality: Implement a search endpoint that allows users to search for events by title, date, or location.

* **Deployment**: Deploy the API to a cloud service.
* **Documentation**: Provide a detailed README file with instructions on how to set up and test the API. Use Swagger for API documentation. Additional features will be bonus - Submission: The final submission on github publick should include: Source code. A link to the deployed API. A README file with setup and usage instructions.
