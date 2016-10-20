from users.users_csv import *
from users.users_load import *


def main():
    new = ReadFile('users.csv')
    new_data = new.data
    connect()
    create_tables()

    for i in new_data:
        # insert_user_list(i)
        print(i)


if __name__ == '__main__':
    main()
