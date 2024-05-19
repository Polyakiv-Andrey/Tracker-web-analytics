# Tracker Web Analytics

Tracker Web Analytics is a web application for analytics, built using Django for the backend and React for the frontend. This project uses PostgreSQL as the database.

## Prerequisites

To run this project, you need to have Docker and Docker Compose installed.

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Running the Project

1. Clone the repository:

   ```bash
   git clone git@github.com:Polyakiv-Andrey/Tracker-web-analytics.git
   cd tracker-web-analytics

2. Start Docker Compose:
    ```bash
    docker-compose up --build
   
This command will build and start the containers for the backend (Django), frontend (React), and the database (PostgreSQL).


3. Access the application:
 * Django server will be available at: http://localhost:8000
 * React app will be available at: http://localhost:3000

## Project Structure
```bash
tracker-web-analytics/
├── backend/
│   ├── Dockerfile
│   ├── manage.py
│   ├── requirements.txt
│   ├── tracker/
│   └── apis/
├── frontend/
│   ├── Dockerfile
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── .env
├── docker-compose.yml
└── README.md
