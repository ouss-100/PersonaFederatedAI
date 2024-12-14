import pandas as pd
import joblib
import requests




model = joblib.load('model.pkl')

new_data = pd.DataFrame({
    'gender': ['male'],
    'relationship_status': ['single'],
    'education': ['Bachelor\'s'],
    'location': ['New York'],
    'sports': [['Soccer', 'Basketball']],
    'favorite_teams': [['New York Knicks']],
    'friends_count': [3000],
    'posts_count': [250],
    'likes_count': [500],
    'music_count': [20]
})



predictions = model.predict(new_data)
print(predictions)


data_to_send = {'predictions': predictions.tolist()}

server_url = "http://127.0.0.1:5000/upload_predictions"
response = requests.post(server_url, json=data_to_send)

if response.status_code == 200:
    print("Predictions successfully sent to the server!")
else:
    print(f"Failed to send predictions: {response.text}")



