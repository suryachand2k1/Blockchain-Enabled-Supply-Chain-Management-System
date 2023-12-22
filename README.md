# Blockchain-Enabled Supply Chain Management System

## Overview
This project integrates blockchain technology into supply chain management, offering enhanced security, transparency, and efficiency. It includes a Python-based blockchain implementation, a Django web application for user interaction, and a MySQL database for data management.

## System Architecture
- **Blockchain Backend**: Python implementation managing blockchain operations.
- **Django Frontend**: Web interface for user interaction with the blockchain.
- **MySQL Database**: Stores user data and transaction details.

## Key Components

### Python Blockchain Implementation
- `Block.py` and `Blockchain.py`: Handle the creation and management of blockchain blocks, ensuring data integrity and secure transactions.

### Django Web Application
- `manage.py`: Facilitates administrative tasks for the Django application.

## MySQL Database Setup
- **Database**: `Supplychain` for managing user and transaction data.
- **Tables**: 
  - `register`: Stores user registration details (`username`, `password`, `contact`, `email`, `address`, `usertype`).

## System Requirements
- Python 3.x
- Django 2.x or higher
- MySQL
- Required Python libraries: `hashlib`, `json`, `time`, `pickle`, `datetime`, `random`, `pyaes`, `pbkdf2`, `binascii`, `os`, `secrets`

## Installation & Configuration
1. Clone the repository and install Python dependencies.
2. Set up the Django environment and run migrations.
3. Configure MySQL database based on provided SQL commands.
4. Start the Django server for web application access.

## Usage Guide

### Blockchain Operations
- Manage blockchain functionality through the Python scripts.

### Django Interface
- Access and interact with the blockchain system via the web interface at `http://localhost:8000`.

## Documentation
Includes a literature review on blockchain applications in supply chain management.

## Contributing
Adhere to Python and Django contribution guidelines for submitting pull requests or issues.

## License
[Specify License Here]

## Contact Information
[Provide Contact Information Here]
