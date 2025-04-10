# Task Management APP

A simple task management APP built using **FastAPI**, **SQLAlchemy**, and **MySQL**, supporting user authentication and task CRUD operations.

---

## Features

- JWT-based user authentication
- Task creation, listing, update, and deletion
- Only authenticated users can create/manage their tasks
- Secure password hashing
- Timestamps for task creation and updates

---

## Technologies Used

- Python 3.10+
- FastAPI
- SQLAlchemy
- PyMySQL
- MySQL Database

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/TaskManagement-FastAPI.git
cd TaskManagement-FastAPI
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
# On Linux source venv/bin/activate
# On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### 3. Configure Database
Make sure you have MySQL running, and create a database:
```sql
CREATE DATABASE TaskDB;
```
Then update your MySQL URL inside `TaskApp/Database.py`:
```python
DATABASE_URL = "mysql+pymysql://username:password@localhost/TaskDB"
```

### 4. Run the Server
```bash
uvicorn TaskApp.main:app --reload
```

---

## API Endpoints
```
  Base Url : http://127.0.0.1:8000  
```
### Auth
- `POST /registration` - Register a new user
- `POST /login/` - Get JWT token `
 
   While login put email on username field . Because of using OAuth2PasswordRequestForm 
  ![login](https://github.com/user-attachments/assets/775001fc-75f8-42d8-958e-c608bf96f4fd)

### Tasks
- `GET /tasks/` -            Get all user's tasks with user informations (Auth required)
 
- `GET /tasks/individual/ -  Get only logged user tasks with his/her information (Auth required)
 
- `GET /tasks/{id}` -        Retrieve specific task (Auth required)
 
- `POST /tasks/` -           Create new task (Auth required)
 
- `PUT /tasks/{id}` -        Update a task (Only by owner) (Auth required)
 
- `PATCH /tasks/{id}` -      Partially update a task (Only by owner) (Auth required)
 
- `DELETE /tasks/{id}` -     Delete task (Only by owner) (Auth required)

---

## Models

### User
- id
- username
- email
- password (hashed)

### Task
- id
- title
- description
- created_at
- updated_at
- user_id (foreign key)

---

## Made With 💖 By
## Rupak Biswas
