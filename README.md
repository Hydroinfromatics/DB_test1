That's great to hear you've deployed the API! Here's an updated version of the `README.md` tailored to include deployment details:

---

# Flask MySQL API

A RESTful API built with Flask to manage user data, deployed for seamless access to features like adding users, retrieving records, and fetching weekly and monthly data.

---

## Features

- **Add Users:** Validate and add new users to the database.
- **Retrieve Data:**
  - Fetch all user records.
  - Fetch records created in the last week or month.
- **Validation:** Ensures proper input for `name`, `email`, and `age` fields.
- **Database Integration:** Connected to a MySQL database.
- **Deployed:** Available as a live service for production use.

---

## Live Deployment

**Base URL:** [https://db-test1-3hdo.onrender.com](https://your-api-domain.com)  



### API Endpoints:

1. **Add User**:  
   `GET /users?name={name}&email={email}&age={age}`  
   Adds a user to the database with validation.  
   Example:  
   ```http
   https://your-api-domain.com/users?name=John&email=john@example.com&age=25
   ```

2. **Get All Users**:  
   `GET /users/all`  
   Retrieves all user records.  
   Example:  
   ```http
   https://your-api-domain.com/users/all
   ```

3. **Get Weekly Data**:  
   `GET /users/weekly`  
   Fetches records created in the last 7 days.  
   Example:  
   ```http
   https://your-api-domain.com/users/weekly
   ```

4. **Get Monthly Data**:  
   `GET /users/monthly`  
   Fetches records created in the last 30 days.  
   Example:  
   ```http
   https://your-api-domain.com/users/monthly
   ```

---

## How to Test Locally

If you want to run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up a `.env` file with the following:
   ```env
   DB_HOST=your-database-host
   DB_USER=your-database-username
   DB_PASSWORD=your-database-password
   DB_NAME=your-database-name
   ```

4. Run the app:
   ```bash
   flask run
   ```

5. Access it locally at `http://127.0.0.1:5000`.

---

## Deployment Details

The API is deployed using the following stack:
- **Platform:** Render
- **WSGI Server:** Gunicorn
- **Database:** MySQL hosted at `AIVEN` (mention host details if public)

To deploy updates:
1. Push changes to your GitHub repository.
2. Ensure your deployment service auto-builds or manually redeploy.

---

## Database Schema

The API uses the following database schema:

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

- **Flask**: Backend framework
- **MySQL**: Database
- **Gunicorn**: WSGI server
- **Python 3.11**: Programming language

---

## Contact

For any issues, reach out to: [gurudev@iccwindia.org](mailto:your-email@example.com)
