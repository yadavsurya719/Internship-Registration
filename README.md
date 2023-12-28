# Internship Registration System

## Overview

The Internship Registration System is a simple Flask web application that allows users to register for internships. The application uses Flask, Flask-SQLAlchemy, and MySQL for database interaction.

## Author

- **Author:** Surya Yadav

## Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy
- MySQL (with a database named 'data')

## Database Connection

Ensure you have a MySQL database named 'data' with the following connection details:

- **Host:** localhost
- **Username:** root
- **Password:** surya7993290146

## How to Use

1. Run the Flask application using the command `python app.py` in the terminal.
2. Access the registration form by navigating to `http://127.0.0.1:5000/register` in a web browser.
3. Fill in the required information and submit the registration form.
4. Successful registrations will display a "Registration Successful!" message.

## Project Structure

- `app.py`: Main Flask application script.
- `templates/register.html`: HTML template for the registration form.

## CSS Styling

The registration form is styled using inline CSS for simplicity. You can customize the styles in the `<style>` tag within the HTML template.

## Acknowledgments

The Internship Registration System uses the following technologies:
- Flask: Web framework for Python.
- Flask-SQLAlchemy: Flask extension for interacting with SQL databases.

## License

This project is licensed under the [MIT License](LICENSE).

