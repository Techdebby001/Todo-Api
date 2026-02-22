# Django To-Do API

A simple full-stack To-Do application built with **Django** that demonstrates how a frontend application communicates with a backend API using REST principles.

This project was built as part of my backend development learning journey to understand API design, data flow between frontend and backend, and CRUD operations.

---

##  Features

- Create,retrieve,update,and delete to-do items (CRUD)
- RESTful API endpoints
- Backend built with Django
- Frontend consumes data from the backend API
- Demonstrates frontend–backend integration
- Simple and clean project structure

---

##  Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, JavaScript  
- **Database:** SQLite (default Django database)  
- **API Style:** REST  

---
##  API Endpoints

Base URL (Local Development):
http://127.0.0.1:8000/

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /get-all-todo/ | Retrieve all todo items |
| POST   | /create-todo/ | Create a new todo item |
| GET    | /get-todo/<id>/ | Retrieve a single todo item |
| PUT    | /update-todo/<id>/ | Update an existing todo item |
| DELETE | /delete-todo/<id>/ | Delete a todo item |

### Example

DELETE request example:
http://127.0.0.1:8000/delete-todo/6/

---

##  Installation & Setup

Follow the steps below to run this project locally:
Run the following command in your terminal (Git Bash, CMD, or Mac Terminal):

### 1️⃣ Clone the repository
git clone https://github.com/Techdebby001/Todo-Api.git
cd Todo-Api

---

### 2️⃣ Create and activate a virtual environment
python -m venv venv

Activate it:
**On Mac/Linux:**
source venv/bin/activate
**On Windows:**
venv\Scripts\activate

---

### 3️⃣ Install dependencies
pip install -r requirements.txt

---

### 4️⃣ Run migrations
python manage.py migrate

---

### 5️⃣ Start the development server
python manage.py runserver

Open your browser and go to:
http://127.0.0.1:8000/

---

## API Testing
- Postman
- Browser (for GET request)

---
## What I Learned

- How to build RESTful APIs with Django

- How frontend applications consume backend APIs

- Managing data flow between frontend and backend

- Structuring backend projects for scalability

- Practical experience with CRUD operations

---
## SCREENSHOTS SECTIONS
<img width="1348" height="502" alt="Screenshot 2026-02-07 112216" src="https://github.com/user-attachments/assets/d1930a4b-fe22-4df2-8ec6-c24b6985e4af" />
<img width="1216" height="631" alt="Screenshot 2026-02-07 112425" src="https://github.com/user-attachments/assets/6ff3f3d4-1e9c-457f-9023-7e2aa4fbc328" />
<img width="1265" height="676" alt="Screenshot 2026-02-07 113329" src="https://github.com/user-attachments/assets/9d146f18-076e-4124-a478-dcac078350e9" />
<img width="1228" height="603" alt="Screenshot 2026-02-07 113354" src="https://github.com/user-attachments/assets/51d85bb9-09a6-4e95-ad1f-2b7dd22e9e04" />
<img width="1272" height="680" alt="Screenshot 2026-02-07 112108" src="https://github.com/user-attachments/assets/50613a77-40bf-4c6d-8f3e-f3295bc0e1fe" />


