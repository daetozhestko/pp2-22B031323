import csv
import psycopg2

# Connect to the database
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="Imnotgay100", port=5432)
cur = conn.cursor()

# Create the contacts table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(20) UNIQUE NOT NULL
    )
""")

# Insert data from CSV file
with open('contacts.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip the header row
    for row in reader:
        name, phone = row[0], row[1]
        cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))

# Insert data from console
name = input("Enter name: ")
phone = input("Enter phone number: ")
cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))

# Update data
user_id = input("Enter user ID: ")
new_name = input("Enter new name (leave blank to keep current): ")
new_phone = input("Enter new phone number (leave blank to keep current): ")
if new_name:
    cur.execute("UPDATE contacts SET name = %s WHERE id = %s", (new_name, user_id))
if new_phone:
    cur.execute("UPDATE contacts SET phone = %s WHERE id = %s", (new_phone, user_id))

# Query data
print("Query Data with filters:")
cur.execute("SELECT * FROM contacts WHERE name LIKE %s", ('Damely%',))
print(cur.fetchall())

cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", ('1261%',))
print(cur.fetchall())

# Delete data
delete_choice = input("Would you like to delete a contact? (y/n)")
if delete_choice == 'y':
    delete_field = input("Delete by name or phone number? (name/phone)")
    if delete_field == 'name':
        delete_name = input("Enter name:")
        cur.execute("DELETE FROM contacts WHERE name = %s", (delete_name,))
    elif delete_field == 'phone':
        delete_phone = input("Enter phone number:")
        cur.execute("DELETE FROM contacts WHERE phone = %s", (delete_phone,))
    else:
        print("Invalid option.")

# Commit the changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()