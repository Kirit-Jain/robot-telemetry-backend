# Mock Robot Telemetry & Data Pipeline

## Project Overview

This project is a robust backend system designed to ingest, process, and store real-time telemetry data from a simulated fleet of construction robots. It mimics a production-grade robotics platform where high-volume sensor data (location, battery levels, status) needs to be reliably collected and made accessible via APIs.

This project was built to demonstrate expertise in Python backend development, containerization, and database architecture, specifically targeting requirements for robotics software engineering roles.

## Architecture & Tech Stack

The system is composed of three distinct microservices orchestrated via Docker Compose:

**1. The Robot Simulator (Python)**

   * **Role:** Acts as the "Edge Device" or Robot Fleet.

   * **Function:** Generates realistic, randomized telemetry data (Robot ID, GPS Coordinates, Battery Voltage) using the `faker` library.

   * **Behavior:** Asynchronously pushes JSON data to the Backend API via HTTP POST requests, simulating real-time field operations.

**2. The Backend API (FastAPI)**

   * **Role:** The central control plane and data gateway.

   * **Tech:** Python 3.11, FastAPI, Pydantic, SQLAlchemy.

   * **Key Features:**

     * **High Performance:** Asynchronous request handling for high-throughput data ingestion.

     * **Data Validation:** Strict schema validation using Pydantic models to ensure data integrity.

     * **Auto-Documentation:** Interactive API documentation (Swagger UI) generated automatically.

**3. The Database (PostgreSQL)**

   * **Role:** Persistent storage layer.

   * **Tech:** PostgreSQL 15 (Dockerized).

   * **Schema:** Relational model optimized for time-series telemetry data storage.

## Setup & Installation

**Prerequisites**

* Docker Desktop (must be running)

* Git


**Running the Project**

1. Clone the repository:

   ```
   git clone https://github.com/Kirit-Jain/robot-telemetry-backend.git
   cd robotics_backend
   ```

2. Launch the Backend Services: Run the following command to build the API image and start the database container:

   ```
   docker-compose up --build -d
   ```

3. Start the Robot Simulator: Open a new terminal and run the simulation script to start generating data:

   ```
   cd simulator
   pip install -r requirements.txt
   python simulate.py
   ```

4. Access the Dashboard: Open your browser to view the interactive API documentation:

   URL: `http://localhost:8000/docs`


## API Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/telemetry/` | Ingest new telemetry data point from a robot. |
| `GET` | `/telemetry/{robot_id}` | Retrieve historical data for a specific robot. |
| `GET` | `/` | Health check endpoint. |

## Key Learnings & Features

* **Dockerization:** Full containerization ensures the environment is reproducible on any machine (local or cloud).

* **Microservices Pattern:** Decoupled the data generation (simulator) from the data ingestion (API) to mimic real-world distributed systems.

* **ORM Implementation:** Used SQLAlchemy for safe, SQL-injection-proof database interactions.
