import argparse
import os
import sys

from integrations.api import ExternalApi
from integrations.gui import ExternalGui
from schema import Spreadsheet


def main(file_path, application_type):
    spreadsheet = Spreadsheet(file_path)
    spreadsheet.read()
    if application_type == 'api':
        service = ExternalApi(
            os.getenv("BASE_URL"),
            os.getenv("AUTH_ENDPOINT"),
            os.getenv("DATA_ENDPOINT"),
            os.getenv("USERNAME"),
            os.getenv("PASSWORD")
        )
    elif application_type == 'gui':
        service = ExternalGui(
            os.getenv("BASE_URL"),
            os.getenv("AUTH_ENDPOINT"),
            os.getenv("DATA_ENDPOINT"),
            os.getenv("USERNAME"),
            os.getenv("PASSWORD")
        )
    else:
        raise Exception("invalid application type")
    service.authenticate()
    for data in spreadsheet.data:
        try:
            service.send_data(data)
        except Exception as e:
            print(f"error sending data: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read excel data and sends to external application")
    parser.add_argument("file_path", help="Excel file path")
    parser.add_argument("application_type", help="External Application type (api or gui)")
    if len(sys.argv) < 3:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
    main(args.file_path, args.application_type)
