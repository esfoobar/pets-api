## "Professional REST API Design using Python Flask"

### Section 1 - Introduction

#### 1.1 Introduction

- What do we want to accomplish in this course?
- Prerequisites
- What do I need to have to complete this course?

#### 1.2 Introduction to API and REST
- What is an API?
- What is REST
    - The six constraints

### Section 2 - A simple API - Pet Store
#### 2.1 Set up core environment
- Using Cloud9 or Docker Client
- Docker client for Mac
    - Docker compose
- Check out the Git repo

#### 2.2 Our first GET/POST
- Using Flask pluggable views
    - Explain Flask [pluggable views](http://flask.pocoo.org/docs/0.11/views/)
- Our first endpoint, /pets
    - A simple GET pluggable view
    - Using [Postman](https://www.getpostman.com/)
    - A simple POST handler (without 201)
- On the POST we should return a 201
    - Talk about [HTTP Codes](http://www.restapitutorial.com/httpstatuscodes.html)
    - Add the 201 to the response
    - Resend the request on Postman

#### 2.3 A Real CRUD
- Build a GET individual pet endpoint
- Add location to all pets (HATEOAS)
- Implement PUT, DELETE on pets

#### 2.4 Simple Authentication
- Write a decorator to allow the user to access the API
- Add authentication to headers in Postman

#### 2.5 Token Based authentication
- Create the app registration endpoint
- Create the token generator
- Build the token-based application access decorator

#### 2.6 An Example Frontend Client
- Using jQuery

### Section 3 - Using Flask-Restful

### Section 4 - The FlaskBook API
