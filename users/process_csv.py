"""
Extract : Read data from CSV file
Transform: Check and Standarise the format of the data extracted from CSV file
"""

from users.exceptions import *
from users.formats import name_format, email_format
import csv
import os
import re

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
        self.localdir = '../data/'
        self.filename = filename
        self.filepath = os.path.join(self.localdir, self.filename)
        self.read_data()

    def read_data(self):
        try:
            csv_in = open(self.filepath, 'rU')
            rows = csv.reader(csv_in, dialect='CSV_reader')
            self.format_data(rows)
            csv_in.close()
        except CouldNotReadFileError as ex:
            print(ex)

    def format_data(self, rows):
        for row in rows:
            name = row[0].title()
            surname = row[1].title()
            email = row[2].lower()
            validate_email = re.match(email_format, email)
            try:
                self._data.append(
                    ''.join(c for c in name + "\t \t" + surname + "\t \t" + email if c not in name_format))

                # if validate_email is None:
                #     raise InvalidEmailError()

            except CouldNotFormatDataError as ex:
                print(ex)

    def get_data(self):
        try:
            return self._data
        except CouldNotGetDataError as ex:
            print(ex)
