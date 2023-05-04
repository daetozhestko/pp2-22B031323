import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="Imnotgay100", port=5432)

# Define a function to return all records based on a pattern
def search_records(pattern):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM contacts WHERE name LIKE %s OR phone LIKE %s", (f'%{pattern}%', f'%{pattern}%'))
        return cur.fetchall()

# Define a procedure to insert or update a user by name and phone
def insert_or_update_user(name, phone):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM contacts WHERE name = %s", (name,))
        if cur.rowcount == 0:
            cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
        else:
            cur.execute("UPDATE contacts SET phone = %s WHERE name = %s", (phone, name))
        conn.commit()

# Define a procedure to insert many new users by list of name and phone
def insert_users(users):
    invalid_users = []
    with conn.cursor() as cur:
        for user in users:
            name, phone = user
            if not phone.isdigit():
                invalid_users.append(user)
            else:
                cur.execute("SELECT * FROM contacts WHERE name = %s", (name,))
                if cur.rowcount == 0:
                    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
                else:
                    cur.execute("UPDATE contacts SET phone = %s WHERE name = %s", (phone, name))
        conn.commit()
    return invalid_users

# Define a function to query data from the tables with pagination
def query_data(limit, offset):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM contacts ORDER BY name LIMIT %s OFFSET %s", (limit, offset))
        return cur.fetchall()

# Define a procedure to delete data from tables by username or phone
def delete_data(pattern):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM contacts WHERE name LIKE %s OR phone LIKE %s", (f'%{pattern}%', f'%{pattern}%'))
        conn.commit()

user_list = [("Zhanibek", "8998"), ("Kyran", "9875"), ("Puerto", "75555")]
insert_users(user_list)

# Close the database connection when finished
conn.close()