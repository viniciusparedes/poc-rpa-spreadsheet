# Project Title

This project reads data from an Excel spreadsheet, processes it, and sends it to an external application using authentication.

## Prerequisites

- Python 3.12.0
- `pip` (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Configuration

Set the following environment variables with your authentication details:

- `AUTH_URL`: The URL for the authentication endpoint.
- `AUTH_DATA_ENDPOINT`: The URL to send data after authenticated.
- `AUTH_USER`: Your username.
- `AUTH_PASS`: Your password.

## Usage

!. Run the main script:
   ```bash
   python main.py <path_to_excel_file>
   ```

This will read the data from the Excel file, authenticate with the external application, and send the data.
