Here’s a `README.md` file tailored for your Flask API project:

---

# Flask MySQL API

A RESTful API built with Flask to manage user data, including functionalities to add users, retrieve all records, and fetch weekly and monthly data.

---

## Features

- **Add Users:** Validate and add new users to the database.
- **Retrieve Data:**
  - Fetch all user records.
  - Fetch records created in the last week or month.
- **Validation:** Ensures proper input for `name`, `email`, and `age` fields.
- **Database Integration:** Connects seamlessly with a MySQL database.

---

## API Endpoints

### 1. **Add a User**
**Endpoint:** `GET /users`  
**Description:** Add a new user to the database.

**Query Parameters:**
| Parameter | Type   | Description                              |
|-----------|--------|------------------------------------------|
| `name`    | String | User's name (max 35 characters).         |
| `email`   | String | User's email (valid `.com/.org/etc`).    |
| `age`     | Int    | User's age (must be between 10 and 100). |

**Example Request:**
```http
GET /users?name=John%20Doe&email=johndoe@example.com&age=30
```

**Example Response:**
```json
{
  "message": "User added successfully",
  "id": 1
}
```

---

### 2. **Get All Users**
**Endpoint:** `GET /users/all`  
**Description:** Fetch all user records.

**Example Response:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com",
    "age": 30,
    "created_at": "2024-12-01T10:00:00Z"
  }
]
```

---

### 3. **Get Weekly Data**
**Endpoint:** `GET /users/weekly`  
**Description:** Fetch user records created in the last 7 days.

**Example Response:**
```json
[
  {
    "id": 2,
    "name": "Jane Doe",
    "email": "janedoe@example.com",
    "age": 25,
    "created_at": "2024-12-05T10:00:00Z"
  }
]
```

---

### 4. **Get Monthly Data**
**Endpoint:** `GET /users/monthly`  
**Description:** Fetch user records created in the last 30 days.

**Example Response:**
```json
[
  {
    "id": 3,
    "name": "Alice",
    "email": "alice@example.com",
    "age": 40,
    "created_at": "2024-12-03T10:00:00Z"
  }
]
```

---

## Installation

### 1. Clone the Repository:
```bash
git clone https://github.com/your-username/your-api-repo.git
cd your-api-repo
```

### 2. Set Up the Environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 4. Configure the `.env` File:
```env
DB_HOST=your-database-host
DB_USER=your-database-username
DB_PASSWORD=your-database-password
DB_NAME=your-database-name
```

---

## Deployment

### Run Locally:
```bash
flask run
```

### Deploy with Gunicorn:
```bash
gunicorn test3:app
```

---

## Database Schema

Run the following SQL to set up the required table:

```sql
CREATE TABLE test_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(35) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Tools and Technologies

- **Flask**: Lightweight web framework for building APIs.
- **MySQL**: Relational database management system.
- **Gunicorn**: Production-ready WSGI server.
- **Python 3.11**: Programming language used for development.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

Let me know if you'd like help with further customization!
