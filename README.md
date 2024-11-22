*Flask Application: User Management API*


Overview

This is a simple Flask application for managing user information, including creating, reading, updating, and deleting (CRUD) users. It uses a MySQL database to store user data.

Setup Instructions
1. Prerequisites
 Python: Version 3.8 or higher.

 MySQL: Ensure MySQL is installed and running.



2. Installation
 Create a virtual environment:
>> python -m venv venv

 Activate the virtual environment:

>>Windows: venv\Scripts\activate
 >>macOS/Linux: source venv/bin/activate

3. Set Up the Database:
 Open a MySQL client and create the database and table:

>>sql code:

CREATE DATABASE users_db;

USE users_db;

CREATE TABLE Users (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255),
    Role VARCHAR(255)
);
Insert sample data:
sql code
INSERT INTO Users (Name, Email, Role) VALUES 
('John Doe', 'john.doe@example.com', 'Admin'),
('Jane Smith', 'jane.smith@example.com', 'Editor');

4. Run the Flask Application

Start the Flask server:
Terminal Command >>flask run
Open your browser and go to:

>>http://127.0.0.1:5000


Additional Notes
Make sure MySQL is running before starting the application.
All dependencies are listed in requirements.txt. If any issues arise during installation, ensure Python and MySQL versions are compatible.
