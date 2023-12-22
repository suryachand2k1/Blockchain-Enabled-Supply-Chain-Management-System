# Blockchain-Enabled Supply Chain Management System

## Overview
This project integrates blockchain technology into supply chain management, offering enhanced security, transparency, and efficiency. It comprises a Python-based blockchain implementation and a Django web application for interface management.

## Key Components

### Python Blockchain Implementation
- `Block.py`: Defines the `Block` class to create blockchain blocks. Each block includes an index, list of transactions, timestamp, previous block's hash, and a nonce for mining.
- `Blockchain.py`: Builds upon `Block.py` to create a blockchain. It includes methods for adding new blocks, validating the chain, and ensuring data integrity through SHA-256 hashing.
- `manage.py`: A Django management script to handle web application tasks like server running, database migrations, and administrative functions.

### Django Web Application
- Part of a Django project named `SupplyChain`.
- Facilitates user interaction with the blockchain system.
- Manages data input and retrieval from the blockchain.

## System Requirements
- Python 3.x
- Django 2.x or higher
- Libraries: `hashlib`, `json`, `time`, `pickle`, `datetime`, `random`, `pyaes`, `pbkdf2`, `binascii`, `os`, `secrets`

## Installation
1. Clone the repository: `git clone [Repository-URL]`
2. Install dependencies: `pip install -r requirements.txt`
3. Initialize Django settings: `export DJANGO_SETTINGS_MODULE=SupplyChain.settings`
4. Run Django migrations: `python manage.py migrate`
5. Start the Django server: `python manage.py runserver`

## Usage

### Blockchain Operations
- Initialize and manage the blockchain.
- Add transactions and mine new blocks.
- Verify blockchain integrity.

### Django Interface
- Access the web interface at `localhost:8000` after running the server.
- Interact with the blockchain system through the web interface.

## Documentation
Includes a systematic literature review on blockchain applications in supply chain management, emphasizing decentralized data management and security.

