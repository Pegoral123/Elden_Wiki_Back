# Elden Wiki - Backend

This repository contains the backend of **Elden Wiki**, a full-stack project dedicated to creating a community-driven repository about the Elden Ring universe.

The backend is responsible for providing a REST API to serve data to the frontend, manage requests, and handle business logic.

## Project Goals

- Serve structured game data and lore to the frontend.
- Provide endpoints for future features like comments, user registration, and authentication.
- Demonstrate and practice backend development skills, including API design, database modeling, and server deployment.

## Technologies Used

| Technology | Role |
|------------|------|
| Python     | Core programming language for the backend. |
| FastAPI    | High-performance framework for building the REST API. |
| Uvicorn    | ASGI server to run the backend application. |
| SQLAlchemy (future) | ORM for relational database integration (MySQL planned). |

## Future Implementations (Roadmap)

- System for comments and user registration.
- Integration with MySQL for relational database modeling.
- Secure authentication with Two-Factor Verification via email.
- Cloud deployment (AWS, Azure, or Google Cloud) to make the API publicly accessible.

## How to Run the Project (Backend)

### Prerequisites

- Python 3.10+ installed
- pip installed
- (Optional) Virtual environment

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/Pegoral123/Elden_Wiki_Back.git

2. **Navigate to the project directory:**
   ```bash
    cd Elden_Wiki_Back

3. **Create a virtual environment:**
   ```bash
    python -m venv venv
    
   
4. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    
5. **Start the backend server:**
    ```bash
    uvicorn main:app --reaload
