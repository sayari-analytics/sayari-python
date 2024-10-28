
# Python Scripts for Sayari API Integration

This repository contains various Python scripts designed to interact with the Sayari API. These scripts include functionalities such as searching for entities, resolving CSV files, loading environment variables, and screening for trade data. Below is a description of each script and its purpose.

## Files

### 1. `csv-resolve.py`
This script reads a CSV file (`entities_to_screen.csv`) and resolves the entities listed in it using the Sayari API. The script performs the following operations:
- Reads the CSV file.
- Extracts entity information (name, address, country) from the CSV rows.
- Uses the `client.resolution.resolution` function to resolve each entity.
- Prints the label of the first resolved entity.

### 2. `env_loader.py`
This script is used to load environment variables from a `.env` file and authenticate the Sayari client. Key operations include:
- Verifying the Python version (requires Python 3.9 or higher).
- Loading `CLIENT_ID` and `CLIENT_SECRET` from environment variables.
- Authenticating with the Sayari API using these credentials.

### 3. `hello-world.py`
This is a basic script that demonstrates how to use the Sayari API. It includes:
- Searching for entities with a specific search term.
- Performing resolution for an entity.
- Conducting traversal and ownership checks, including beneficial ownership (UBO).
- Checking watchlists and performing shortest path traversal.
- Fetching API usage and history.

### 4. `screening.py`
This script performs a screening of a specific entity (in this case, 'Microcenter'). It searches for:
- Shipments.
- Suppliers.
- Buyers.
The results are printed out to show how many shipments, suppliers, or buyers were found.

### 5. `smoke-test.py`
A smoke test script designed to test the basic functionality of the Sayari API, ensuring that key API endpoints are working as expected:
- Resolving entities.
- Checking beneficial ownership.
- Conducting traversal of entities.

### 6. `trade-search.py`
This script interacts with the Sayari API to search for trade data related to a specific search term ('Microcenter'). It checks for:
- Shipments.
- Suppliers.
- Buyers.

## Setup

### Prerequisites
- Python 3.9 or higher
- `pip` installed for package management
- A `.env` file with the following variables:
  - `CLIENT_ID`
  - `CLIENT_SECRET`
  - `BASE_URL` (optional, defaults to Sayari production environment)

### Installation

1. Clone this repository.
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the `.env` file with the required environment variables.
4. Run any of the scripts:
   ```bash
   python <script_name>.py
   ```