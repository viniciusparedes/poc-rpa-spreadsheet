import pandas


class Data:
    name: str = None
    birthday: str = None
    document_number: str = None
    document_type: str = None

    def __init__(self, name, birthday, document_number, document_type):
        self.name = name
        self.birthday = birthday
        self.document_number = document_number
        self.document_type = document_type


class Spreadsheet:
    _path = None
    data: list[Data] = []

    def __init__(self, path):
        self._path = path

    def read(self):
        if not self._path:
            raise ValueError("no path provided!")
        try:
            data = pandas.read_excel(self._path)
        except Exception as e:
            raise ValueError(f"error reading file: {e}")
        for index, row in data.iterrows():
            try:
                self.data.append(
                    Data(
                        name=row['name'],
                        birthday=row['birthday'].strftime('%Y-%m-%d'),
                        document_number=str(row['document_number']),
                        document_type=row['document_type']
                    )
                )
            except Exception as e:
                raise ValueError(f"error reading row {index}: {e}")
