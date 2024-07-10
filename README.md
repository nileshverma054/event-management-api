# Event-Management-Api

The Event Management RESTful API is a server-side application that allows users to manage events. It provides endpoints for different access levels, allowing users to view events and administrators to manage them. Users can register for events, and administrators can add, remove, or edit events. The API supports search functionality, allowing users to search for events by title, date, or location.

### API Documentation

* [Swagger API Documentation](https://event-management-api-o6iz.onrender.com/docs)

### Repository Link

* [Github](https://github.com/nileshverma054/event-management-api)

---

### TODO

- [x] Project Setup
- [x] API Documentation
- [x] Database Migration with Alembic
- [x] Use pipenv to manage dependencies
- [ ] Events API
    - [x] Add events
    - [x] Get events
    - [x] Edit events
    - [x] Remove events
    - [ ] Register for events
    - [ ] Search functionality for events
- [ ] Authentication
- [ ] Authorization
- [ ] Containerization with Docker and Docker Compose
- [ ] Tests for the API

### Project Setup

**Framework and Database**


**Database Migration**

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

---

### Requirement Details for reference

**Event Management RESTful API**

Objective: Create a RESTful API for managing events.
The API should support different access levels, allowing users to view events and administrators to manage them.

Requirements:

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

* Deployment: Deploy the API to a cloud service.
* Documentation: Provide a detailed README file with instructions on how to set up and test the API. Use Swagger for API documentation. Additional features will be bonus - Submission: The final submission on github publick should include: Source code. A link to the deployed API. A README file with setup and usage instructions.
