import argparse
import os
import sys

from application import ExternalApplication
from schema import Spreadsheet


def main(file_path):
    spreadsheet = Spreadsheet(file_path)
    spreadsheet.read()
    service = ExternalApplication(os.getenv("AUTH_URL"), os.getenv("AUTH_DATA_ENDPOINT"), os.getenv("AUTH_USER"), os.getenv("AUTH_PASS"))
    service.authenticate()
    for data in spreadsheet.data:
        try:
            service.send_data(data)
        except Exception as e:
            print(f"error sending data: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read excel data and sends to external application")
    parser.add_argument("file_path", help="Excel file path")
    if len(sys.argv) < 2:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
    main(args.file_path)
