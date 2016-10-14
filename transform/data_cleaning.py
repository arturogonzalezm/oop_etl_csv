from extract.read_csv import ReadFile


# Clean users data from CSV file.....TODO
class Users(object):
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

