# IBTech-API

## Overview

IBTech-API is a FastAPI-based project that provides a backend service for managing products and users. The project includes JWT authentication, role-based authorization, and CRUD operations for products. It uses SQLAlchemy for ORM and Pydantic for data validation.

## Features

- **JWT Authentication**: Secure user authentication using JSON Web Tokens (JWT).
- **Role-Based Authorization**: Admin and user roles to manage access to various endpoints.
- **Product Management**: CRUD operations for managing products.
- **User Management**: User registration, login, and profile management.
- **PostgreSQL**: Uses PostgreSQL as the database.
- **Docker**: Dockerized for easy deployment and scalability.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/meshalal/IBTech-API.git
    cd IBTech-API/backend
    ```

2. **Set up the environment variables**:
    Create a `.env` file in the root directory and add the following:
    ```env
    DATABASE_URL=postgresql+psycopg2://dev_admin:dev_admin@localhost:5432/testdb
    SECRET_KEY=your_secret_key
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

### Running the Application

1. **Run the application using Docker Compose**:
    
change your directory to the project root, then:

    ```sh
    docker-compose up --build
    ```

2. **Access the API documentation**:
    Open your browser and navigate to `http://localhost:8000/docs` for the interactive API documentation.

