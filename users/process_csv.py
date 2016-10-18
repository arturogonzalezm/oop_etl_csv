"""
Extract : Read data from CSV file
Transform: Check and Standarise the format of the data extracted from CSV file
"""

from users.exceptions import *
from users.formatter import name_format, Email

import csv
import os

csv.register_dialect(
    'CSV_reader',
    delimiter=',',
    quotechar='"',
    doublequote=True,
    skipinitialspace=True,
    lineterminator='\r\n',
    quoting=csv.QUOTE_MINIMAL)


class ReadFile(object):
    def __init__(self, filename):
        self._data = []
        self.local_dir = '../data/'
        self.filename = filename
        self.file_path = os.path.join(self.local_dir, self.filename)
        self.read_data()

    def read_data(self):
        try:
            csv_in = open(self.file_path, 'rU')
            rows = csv.reader(csv_in, dialect='CSV_reader')
            next(rows, None)
            self.format_data(rows)
            csv_in.close()
        except CouldNotReadFileError as ex:
            print(ex)

    def format_data(self, rows):
        for row in rows:
            name = row[0].title()
            surname = row[1].title()
            email = row[2].lower()
            try:
                self._data.append(''.join(c for c in name if c not in name_format))
                self._data.append(''.join(c for c in surname if c not in name_format))

                if email is not None:
                    self._data.append(''.join(c for c in email if c not in name_format))
                    for i in filter(Email.validate_email, [email]):
                        print("Invalid email:", i)

            except CouldNotFormatDataError as ex:
                print(ex)

    @property
    def data(self):
        try:
            return self._data
        except CouldNotGetDataError as ex:
            print(ex)
