# mock-API
This is an assessment assignment for a mock API.


```Service Definition

We require a secure and scalable RESTful API to manage product information within a e-commerce platform. This API will be used by internal systems and potentially external partners to interact with product data.

The API must allow for CRUD (Create, Read, Update, Delete) operations on product resources.

Product resources should include attributes like product name, description, category, price, stock availability, and high-quality image URLs.

The API should enable filtering and searching for products based on various criteria (e.g., category, price range).

Secure authentication and authorization mechanisms are required to control access to the API.

 

Resource Identification

List the core entities (resources) involved in your service. These are the things users will interact with (e.g., products in the catalog)

Define the attributes (data fields) associated with each resource. You don't need to be very detailed.

 

Endpoints

Map the functionalities of your service to HTTP methods (GET, POST, PUT, DELETE) for the relevant resources.

Design URL structures (endpoints) for each functionality. These URLs will be used to access and manipulate resources.

Use nouns to represent resources (e.g., /books, /tasks)

Consider including identifiers for specific resource instances (e.g., /books/{id})

 

Request and Response Schemas

Define the data format used for requests and responses (in JSON).

Create JSON Schemas for both requests and responses. These schemas should specify the structure and data types of the information being exchanged.

Compile your API design choices into a clear and concise document using OpenAPI Schema. You can use the following tool for building the same - https://editor-next.swagger.io/

Consider adding error codes and response structures for potential error scenarios.

Include an example request and response for a specific functionality to illustrate usage.```