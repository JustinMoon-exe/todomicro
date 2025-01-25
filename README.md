# Microservices User Management API

This project is designed to help me learn and implement basic **microservices** concepts using **Flask**. The goal is to build a simple User Management API with registration and login functionality, incorporating best practices like password hashing.

## Description
This project is a simple **User Management API** with two primary functionalities:
- **User Registration**: Allows users to register by providing a username and password. Passwords are securely hashed before being stored.
- **User Login**: Users can log in by providing a username and password. The provided password is checked against the hashed password in the database.

This project will be a step-by-step learning experience, where I will implement additional microservice features and improve security and performance over time.

## Features
- **User Registration**: Users can register with a unique username and password.
- **User Login**: Users can log in by providing their credentials.
- **Password Hashing**: Passwords are securely hashed using `bcrypt` before being stored.
- **Simple Flask API**: The app is built with Flask to keep it lightweight and easy to extend.

## Technologies Used
- **Python**: For the backend logic and Flask server.
- **Flask**: A lightweight Python web framework for building the API.
- **bcrypt**: For securely hashing user passwords.
- **Postman** or **cURL**: For API testing.
- **JSON**: For sending and receiving data.

## Goals
- [x] Set up a basic Flask app with a `/register` endpoint.
- [x] Implement a `/login` endpoint.
- [x] Hash passwords using `bcrypt` for security.
- [ ] Implement a user persistence layer (e.g., store users in a database instead of in-memory).
- [ ] Implement **JWT Authentication** for login sessions.
- [ ] Implement **Role-Based Access Control (RBAC)** for different user roles.
- [ ] Deploy the API using a platform like **Heroku** or **AWS**.
