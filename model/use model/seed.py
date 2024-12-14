#[('Openness', 3.307237891966939), ('Conscientiousness', 70.83383544205002), ('Agreeableness', 0.3839920319212075), ('Extraversion', 24.53438360533133), ('Neuroticism', 0.9405510287305106)]

import mysql.connector
import random

# Database configuration
db_config = {
    'host': 'localhost',   # Your MySQL host
    'user': 'root',        # Your MySQL user
    'password': 'root100', # Your MySQL password
    'database': 'personality' # Your database name
}

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

# Function to insert a single user and their personality values
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
                "INSERT INTO userpersonality (userId, name, value) VALUES (%s, %s, %s)",  # Use `userId`
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
    {"email": "medhgfj.mouhghjib@example.com", "name": "Med Mouhib", "dominantpersonality": "Extraversion"},
    {"email": "amifghjna.khagjflil@example.com", "name": "Amina Khalil", "dominantpersonality": "Openness"}
]

# Call the function for each user with generated personality values
for user in dummy_users:
    personalities = generate_personality_values()
    insert_user(user['email'], user['name'], user['dominantpersonality'], personalities)
