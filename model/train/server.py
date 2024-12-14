import flwr as fl
import tensorflow as tf
import joblib

class SaveModelStrategy(fl.server.strategy.FedAvg):
    def __init__(self, model_save_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_save_path = model_save_path
        self.model = tf.keras.applications.MobileNetV2(input_shape=(32, 32, 3), classes=10, weights=None)
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    def aggregate_fit(self, rnd, results, failures):
        aggregated_weights = super().aggregate_fit(rnd, results, failures)
        
        if aggregated_weights is not None:
            self.model.set_weights(aggregated_weights)
            
            joblib.dump(self.model, self.model_save_path)
            print(f"Model saved to {self.model_save_path} after round {rnd}")
        
        return aggregated_weights

model_save_path = "aggregated_model.pkl"
strategy = SaveModelStrategy(model_save_path=model_save_path)

fl.server.start_server(
    server_address="0.0.0.0:5000",
    config=fl.server.ServerConfig(num_rounds=3),
    strategy=strategy,
)
