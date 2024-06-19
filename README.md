# Accuknox Assignment
 

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)


## Overview

This project is a social networking API built using Django and Django Rest Framework, based on the Accuknox assignment. The project leverages Django Cookiecutter for a structured and scalable project setup, and it is containerized using Docker for ease of deployment and consistency across different environments.

## Features

- **User Authentication:** Sign up and login using email and password.
- **User Search:** Search users by email or name.
- **Friend Requests:** Send, accept, and reject friend requests.
- **Friend List:** List of accepted friends.
- **Pending Requests:** List of received friend requests.
- **Rate Limiting:** Users cannot send more than 3 friend requests within a minute.

## Technologies Used

- **Django Cookiecutter:** Provides a structured project setup with best practices.
- **Django Allauth:** Simplifies authentication with ready-to-use views and forms.
- **JWT Authentication:** Ensures secure communication by encoding user information in tokens.
- **Docker:** Containerizes the application for consistent and reproducible environments.

## Steps to Run the Docker Container 

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/gauravrajaura/accuknox.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd accuknox
    ```

3. **Build and Run the Docker Container Locally:**

   *Ensure that docker compose is installed already and engine is running

    ```bash
    docker-compose -f docker-compose.local.yml build
    docker-compose -f docker-compose.local.yml up
    ```

5. **Access the APIs:**

    Use Postman or any API client to interact with the APIs. You can find the Postman collection here [POSTMAN COLLECTION](https://www.postman.com/material-saganist-86983182/workspace/accuknox/collection/36360618-c9194eab-04bb-4942-a96f-fb1ffd5cd6cd?action=share&creator=36360618&active-environment=36360618-b63f629b-d778-4eba-8430-151f28bd1618).
