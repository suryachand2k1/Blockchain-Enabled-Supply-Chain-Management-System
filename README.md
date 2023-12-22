# Blockchain-Enabled Supply Chain Management System

## Overview
This project harnesses blockchain technology to revolutionize supply chain management. It enhances data security, transparency, and efficiency through a well-integrated system comprising a Python-based blockchain, a Django web application, and a MySQL database.

## System Architecture
- **Blockchain Backend**: Implemented in Python, this component is the heart of the system, handling the creation, management, and integrity verification of blockchain blocks.
- **Django Frontend**: A user-friendly web interface, built with Django, allows users to interact seamlessly with the blockchain, including transaction management and viewing block information.
- **MySQL Database**: Essential for storing user registration details and transaction data, ensuring efficient data retrieval and management.

## Key Components

### Python Blockchain Implementation
- `Block.py` and `Blockchain.py`:
  - **Block.py**: Defines the `Block` class, crucial for blockchain's foundation. It includes key attributes like index, transactions, timestamp, previous hash, and nonce.
  - **Blockchain.py**: Builds on Block.py to create a complete blockchain system. It adds new blocks, validates the chain's integrity, and employs SHA-256 hashing for security.

### Django Web Application
- **manage.py**: A Django script that provides administrative control over the web application. It's used for tasks like starting the server, database migration, and more.

## MySQL Database Setup
- **Database Creation**:
  - `create database Supplychain;`: Creates the main database for the project.
- **Table Structure**:
  - `register`: A pivotal table storing user registration details, comprising username, password, contact information, email, address, and user type.

## System Requirements
- Python 3.x
- Django 2.x or higher
- MySQL
- Python libraries: `hashlib`, `json`, `time`, `pickle`, `datetime`, `random`, `pyaes`, `pbkdf2`, `binascii`, `os`, `secrets`

## Installation & Configuration
1. **Repository Setup**:
   - Clone the repository: `git clone [Repository-URL]`.
   - Navigate to the project directory.
2. **Dependencies**:
   - Install Python packages: `pip install -r requirements.txt`.
3. **Django Setup**:
   - Set Django environment: `export DJANGO_SETTINGS_MODULE=SupplyChain.settings`.
   - Run migrations for database setup: `python manage.py migrate`.
4. **Database Configuration**:
   - Follow the SQL commands in `DB.txt` to set up the MySQL database.
5. **Running the Server**:
   - Start the Django server: `python manage.py runserver`.
   - Access the web interface at `http://localhost:8000`.

## Detailed Usage
### Blockchain Operations
- **Adding Blocks**: Use `Blockchain.py` to add transactions and mine blocks.
- **Chain Validation**: Regularly verify the chain's integrity to prevent data tampering.

### Django Interface
- **Web Interface**: Manage blockchain transactions, view block details, and handle user registrations.

## Example Use Cases
- **Supply Chain Transparency**: Monitor and authenticate the movement of goods.
- **Data Verification**: Maintain data accuracy and security in supply chain records.

