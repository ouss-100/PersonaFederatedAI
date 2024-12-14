#[('Openness', 3.307237891966939), ('Conscientiousness', 70.83383544205002), ('Agreeableness', 0.3839920319212075), ('Extraversion', 24.53438360533133), ('Neuroticism', 0.9405510287305106)]



from flask import Flask, request, send_file, jsonify
import mysql.connector
import random

db_config = {
    'host': 'localhost',   # Your MySQL host
    'user': 'root',        # Your MySQL user
    'password': 'root100', # Your MySQL password
    'database': 'personality' # Your database name
}



import mysql.connector
import random

# Function to generate random personality values summing to 100 for the five personalities
def generate_personality_values():
    value1 = random.random() * 100
    value2 = random.random() * (100 - value1)
    value3 = random.random() * (100 - value1 - value2)
    value4 = random.random() * (100 - value1 - value2 - value3)
    value5 = 100 - (value1 + value2 + value3 + value4)

    values = [value1, value2, value3, value4, value5]
    random.shuffle(values)

    return [
        ("Openness", values[0]),
        ("Conscientiousness", values[1]),
        ("Agreeableness", values[2]),
        ("Extraversion", values[3]),
        ("Neuroticism", values[4]),
    ]


# Function to insert a single user
def insert_user(email, name, dominant_personality, personalities):
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert user data
        cursor.execute(
            "INSERT INTO user (email, name, dominantpersonality) VALUES (%s, %s, %s)",
            (email, name, dominant_personality)
        )
        user_id = cursor.lastrowid  # Get the last inserted user's ID

        # Insert personality data
        for personality in personalities:
            cursor.execute(
                "INSERT INTO userpersonality (user_id, name, value) VALUES (%s, %s, %s)",
                (user_id, personality[0], personality[1])
            )

        # Commit the transaction
        conn.commit()

        print(f"User created: {name} (ID: {user_id})")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the database connection
        cursor.close()
        conn.close()

# Example usage: Insert users one by one
dummy_users = [
    {"email": "medîjgf.mouhibsdgdfsgdfgdsgdfgdf@example.com", "name": "Med Mouhib", "dominantpersonality": "Extraversion"},
]

# Call the function for each user with generated personality values
for user in dummy_users:
    personalities = generate_personality_values()
    insert_user(user['email'], user['name'], user['dominantpersonality'], personalities)


i have this erorr 
Error: 1054 (42S22): Unknown column 'user_id' in 'field list'


this is user table 


mysql> desc  user;
+---------------------+--------------+------+-----+----------------------+-------------------+
| Field               | Type         | Null | Key | Default              | Extra             |
+---------------------+--------------+------+-----+----------------------+-------------------+
| id                  | int          | NO   | PRI | NULL                 | auto_increment    |
| email               | varchar(191) | NO   | UNI | NULL                 |                   |
| name                | varchar(191) | YES  |     | NULL                 |                   |
| dominantpersonality | varchar(191) | YES  |     | NULL                 |                   |
| createdAt           | datetime(3)  | NO   |     | CURRENT_TIMESTAMP(3) | DEFAULT_GENERATED |
+---------------------+--------------+------+-----+----------------------+-------------------+

'''import sqlite3
import random

# Function to generate random percentages summing to 100 for five personalities
def generate_personality_values():
    value1 = random.uniform(0, 100)
    value2 = random.uniform(0, 100 - value1)
    value3 = random.uniform(0, 100 - value1 - value2)
    value4 = random.uniform(0, 100 - value1 - value2 - value3)
    value5 = 100 - (value1 + value2 + value3 + value4)
    
    values = [value1, value2, value3, value4, value5]
    random.shuffle(values)
    
    return [
        ("Openness", values[0]),
        ("Conscientiousness", values[1]),
        ("Agreeableness", values[2]),
        ("Extraversion", values[3]),
        ("Neuroticism", values[4]),
    ]

# Dummy user data
user_data = [
    {"email": "med.mouhib@example.com", "name": "Med Mouhib", "dominantpersonality": "Extraversion"},
    {"email": "sofia.karoui@example.com", "name": "Sofia Karoui", "dominantpersonality": "Openness"},
    {"email": "ali.benhassen@example.com", "name": "Ali Ben Hassen", "dominantpersonality": "Conscientiousness"},
    {"email": "amira.chaouachi@example.com", "name": "Amira Chaouachi", "dominantpersonality": "Agreeableness"},
    {"email": "khaled.zied@example.com", "name": "Khaled Zied", "dominantpersonality": "Neuroticism"},
]

# Create and populate the database
def seed_database(users):
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("personalitytt.db")
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            dominantpersonality TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS userpersonality (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            value REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES user (id)
        )
    """)
    
    # Insert data into tables
    for user in users:
        # Insert user data
        cursor.execute("""
            INSERT INTO user (email, name, dominantpersonality)
            VALUES (?, ?, ?)
        """, (user["email"], user["name"], user["dominantpersonality"]))
        user_id = cursor.lastrowid  # Get the last inserted user's ID

        # Insert personality data
        personalities = generate_personality_values()
        for name, value in personalities:
            cursor.execute("""
                INSERT INTO userpersonality (user_id, name, value)
                VALUES (?, ?, ?)
            """, (user_id, name, value))
    
    # Commit and close connection
    conn.commit()
    conn.close()
    print("Database seeded successfully.")



def tt():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("personalitytt.db")
    cursor = conn.cursor()

    # Create tables
    t= cursor.execute("""
        select * from user
    """)
    print(t.fetchall())

    
    # Commit and close connection
    conn.commit()
    conn.close()
    print("Database seeded successfully.")

# Execute the seeding process
#seed_database(user_data)

tt()

'''