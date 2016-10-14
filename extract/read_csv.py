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
            with open(self.filepath, 'rU') as c:
                rows = csv.reader(c, dialect='CSV_reader')
                for row in rows:
                    self._data.append(row[0].title())
                    self._data.append(row[1].title())
                    self._data.append(row[2].lower())
        except Exception as ex:
            print(ex)

    def get_data(self):
        return self._data
