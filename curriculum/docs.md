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
    - Running the containers separately for pdb
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

#### 2.6 Authentication Testing
- Start a testing framework

#### 2.7 Work on Store API
- Build store models
- Don't expose MongoDB ID, use uuid
- Validation of data using [jsonschema](http://python-jsonschema.readthedocs.io/en/latest/)
  - [Great resource](https://spacetelescope.github.io/understanding-json-schema/index.html) to understanding it
- Build JSON templates

### 2.8 Store PUT and DELETE
- PUT operations are the update of CRUD. It generally receives all the fields with the ones being updated changed.
  - PATCH is used for updating only specific fields (we won't implement)
- Implement DELETE

### 2.9 Implement GET all stores
- Pagination
  - Results should always be paginated
  - Links within show next and prev
    - This is the HATEOAS of the app

### 2.10 Store Testing
- Testing CRUD
- Testing pagination
  - Introduction to Fixtures
  - Custom fixtures using mongoimport

### 2.11 The Pet App
  - Create CRUD

### 2.12 Pet Tests
  - Write Tests

### 2.13 Pet searches
  - Get all pets in a specific store
  - Implementing filters across stores

### Section 3 - Using Swagger to Document your API

#### Bonus - An Example Frontend Client
- Using jQuery
