# Task Management API

A simple task management API built using **FastAPI**, **SQLAlchemy**, and **MySQL**, supporting user authentication and task CRUD operations.

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
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Database
Make sure you have MySQL running, and create a database:
```sql
CREATE DATABASE task_db;
```
Then update your MySQL URL inside `TaskApp/Database.py`:
```python
DATABASE_URL = "mysql+pymysql://username:password@localhost/task_db"
```

### 4. Run the Server
```bash
uvicorn TaskApp.main:app --reload
```

---

## API Endpoints

### Auth
- `POST /register/` - Register a new user
- `POST /login/` - Get JWT token

### Tasks
- `GET /tasks/` - Get logged-in user's tasks
- `GET /tasks/{id}` - Retrieve specific task
- `POST /tasks/` - Create new task (Auth required)
- `PUT /tasks/{id}` - Update a task (Only by owner)
- `PATCH /tasks/{id}` - Partially update a task (Only by owner)
- `DELETE /tasks/{id}` - Delete task (Only by owner)

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

## Example `.env` (if needed)
```
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
MYSQL_DB=task_db
```

---

## Made With 💖
## Rupak Biswas
