# Reverse Polish Notation Calculator

## Summary

The application provides a simple calculator front-end that shows and calculates operations in post-fix notation (IPN).

The operations and the results are persisted in a database and are downloadable by clicking on the **D** button on the calculator.

## Installation

From the root of the project and with Docker running:

`docker compose up`

Given the simplicity of the project and for ease of use the environment variables are hardcoded in the versioned compose.yaml despite best practices.

During build time the backend container uses a shell script to initialize a postgreSQL database(on the default port 5432) which exists in a separate

container and the frontend container bundles the latest build.

## Running the application

1. You can test the build on **localhost:4173**
2. You can read the Swagger API docs on **localhost:8000/docs**

## Notes

As per the documentation the test route has been deprecated as an example of FastAPI's powerful automatic documentation
