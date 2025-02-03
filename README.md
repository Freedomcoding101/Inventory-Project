Inventory Management System

Description

This is a command-line-based Inventory Management System built using Flask, SQLAlchemy, and Python. The system allows users to view, add, and back up products stored in an SQLite database. It reads data from a CSV file, ensures data integrity, and updates inventory as needed. The program provides an interactive menu for managing products, including adding new items, updating prices, and exporting inventory backups.

Features

View Products: Display a list of all products and check stock levels.

Add Products: Insert new products or update existing ones.

Backup Inventory: Export product data to a CSV file.

Data Integrity: Prevents duplicate entries and ensures the latest updates are saved.

User-Friendly CLI: Provides an easy-to-navigate menu for inventory management.

Installation

Prerequisites

Python 3.x installed

Virtual environment (optional but recommended)

Required dependencies in requirements.txt

Setup

Clone the repository:

git clone https://github.com/yourusername/inventory-management.git
cd inventory-management

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Set up the database:

python app.py  # This initializes the database and runs the application

Usage

Run the application:

python app.py

Follow the interactive menu:

Type v to view all products.

Type a to add a new product.

Type b to create a backup of the inventory.

Type exit to close the application.



What I Learned

Using Flask and SQLAlchemy for database management.

Handling user input and validation in a CLI-based program.

Implementing CRUD operations (Create, Read, Update, Delete) in a database.

Working with CSV files to import/export data efficiently.

Structuring a Python project for maintainability and scalability.

Future Improvements

Add a Flask web interface for easier product management.

Implement search and filtering features.

Improve error handling and input validation.

Expand database support for larger-scale usage.

Feel free to modify this README.md to fit your needs!
