
import tensorflow as tf
import flwr as fl
import pandas as pd
import numpy as np
import tensorflow as tf


df = pd.read_csv('dataset.csv')

X = df.drop(columns=["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"])
y = df[["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]]

numeric_features = ["friends_count", "posts_count", "likes_count", "music_count"]
categorical_features = ["gender", "relationship_status", "education", "location"]

numeric_means = X[numeric_features].mean(axis=0)
numeric_stds = X[numeric_features].std(axis=0)
X_numeric = (X[numeric_features] - numeric_means) / numeric_stds

categorical_vocab_dicts = {
    col: {val: idx for idx, val in enumerate(X[col].unique())}
    for col in categorical_features
}
X_categorical = np.hstack([
    np.eye(len(vocab))[X[col].map(vocab).fillna(0).astype(int)]
    for col, vocab in categorical_vocab_dicts.items()
])

X_preprocessed = np.hstack([X_numeric, X_categorical])

split_idx = int(0.8 * len(X_preprocessed))
X_train, X_test = X_preprocessed[:split_idx], X_preprocessed[split_idx:]
y_train, y_test = y.values[:split_idx], y.values[split_idx:]


model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(5)  
])
model.compile(optimizer='adam', loss='mse', metrics=['mae'])





class FlowerClient(fl.client.NumPyClient):
    def get_parameters(self, config):
        return model.get_weights()
    
    def fit(self, parameters, config):
        model.set_weights(parameters)
        model.fit(X_train, y_train, epochs=1, batch_size=32)
        return model.get_weights(), len(X_train), {}

    def evaluate(self, parameters, config):
        model.set_weights(parameters)
        loss, accuracy = model.evaluate(X_test, y_test)
        return loss, len(X_test), {'accuracy': accuracy}

fl.client.start_numpy_client(server_address="127.0.0.1:5000", client=FlowerClient())

