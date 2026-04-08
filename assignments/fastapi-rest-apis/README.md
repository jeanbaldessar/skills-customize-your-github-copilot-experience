# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build and deploy REST APIs using FastAPI, a modern Python web framework. You will create a fully functional API with CRUD operations, request validation, and interactive API documentation.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a new FastAPI project and create the basic structure for a REST API. Initialize the application, install required dependencies, and implement a simple "Hello World" endpoint to verify your setup is working correctly.

#### Requirements
Completed program should:

- Initialize a FastAPI application instance
- Install FastAPI and Uvicorn dependencies
- Implement a GET endpoint at `/` that returns a welcome message
- Run the server and verify the endpoint works (uvicorn main:app --reload)

### 🛠️ Build CRUD Endpoints for a Resource

#### Description
Create a REST API with full CRUD (Create, Read, Update, Delete) operations for a chosen resource (e.g., tasks, notes, books, or students). Implement endpoints that handle different HTTP methods and demonstrate proper API design patterns.

#### Requirements
Completed program should:

- Implement GET endpoint to retrieve all items
- Implement GET endpoint with path parameter to retrieve a specific item
- Implement POST endpoint to create a new item with request validation
- Implement PUT endpoint to update an existing item
- Implement DELETE endpoint to remove an item
- Use appropriate HTTP status codes (200, 201, 404, 400)

### 🛠️ Add Request Validation and Error Handling

#### Description
Implement data validation using Pydantic models to ensure API requests follow the correct format. Add comprehensive error handling to provide meaningful error messages when requests fail validation or resources are not found.

#### Requirements
Completed program should:

- Define Pydantic models for request and response data structures
- Validate incoming requests against defined models
- Return appropriate error responses with descriptive messages
- Handle and return 404 errors when requested resources don't exist
- Handle and return 422 errors for invalid request data
- Provide clear error messages for validation failures

