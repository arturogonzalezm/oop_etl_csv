from users.process_csv import ReadFile


def main():
    new = ReadFile('users.csv')
    new_data = new.data

    for i in new_data:
        print(i)


if __name__ == '__main__':
    main()
