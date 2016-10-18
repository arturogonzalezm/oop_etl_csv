"""
Extract : Read data from CSV file
Transform: Check and Standarise the format of the data extracted from CSV file
"""

from users.exceptions import *
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
            try:
                self._data.append(''.join(c for c in
                                          row[0].title() + "\t \t" +
                                          row[1].title() + "\t \t" +
                                          row[2].lower()
                                          if c not in '/><=+-?!#"  "$%^&*""()" "_+:;'))
            except CouldNotFormatDataError as ex:
                print(ex)
    @property
    def data(self):
        try:
            return self._data
        except CouldNotGetDataError as ex:
            print(ex)


            # TODO

            # verify_email = 'info@emailhippo.com'
            # email_match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', verify_email)
            #
            # if email_match is None:
            #     print('There is a syntax error in the email address')
            #     raise InvalidEmailError('There is a syntax error in the email address')
            # else:
            #     print('Email Address is correct')

            # TODO
