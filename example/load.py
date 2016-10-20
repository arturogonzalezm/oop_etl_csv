import csv

import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port=5432)

print("Opened database successfully")

cursor = conn.cursor()

query = 'INSERT INTO users (name, surname, email) VALUES (%s, %s, %s)'


csv_data = csv.reader(open('../data/users.csv'))


for row in csv_data:
    values = (row[0].title(), row[1].title(), row[2].lower())
    cursor.execute(query, values)
    print("User loaded")
# close the connection to the database.
conn.commit()
cursor.close()
print("\nDone!")
