from flask import Flask, request, send_file, jsonify
import mysql.connector


db_config = {
    'host': 'localhost',   # Your MySQL host
    'user': 'root',        # Your MySQL user
    'password': 'root100', # Your MySQL password
    'database': 'personality' # Your database name
}


def insert_data(user_data, personality):
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute(
                f"INSERT INTO user (email, name, dominantpersonality) VALUES ({10}, %s, %s, %s)",
                (user_data['email'], user_data['name'], user_data['dominantpersonality'])
            )
        user_id = cursor.lastrowid  # Get the last inserted user's ID

        cursor.execute(
                    "INSERT INTO userpersonality (user_id, name, value) VALUES (%s, %s, %s)",
                    (user_id, personality[0], personality[1])
                )

        print(f"User created: {user_data['name']} (ID: {user_id})")

        # Commit the transaction
        conn.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the database connection
        cursor.close()
        conn.close()


app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download_file():
    try:        
        return send_file("model.rar", as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500




@app.route('/upload_predictions', methods=['POST'])
def upload_predictions():
    try:
        predictions = request.json.get('predictions', None)
        if predictions is None:
            return jsonify({"error": "No predictions provided"}), 400
        
        print("Received predictions from the client:", predictions)
        user_data= {'email': "gggggggg", 'name': "jghjnjlj", 'dominantpersonality': 50}
        
        
        return jsonify({"message": "Predictions received successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500




if __name__ == '__main__':
    app.run(debug=True)