import pickle
import numpy as np

# Load the model from the pickle file
try:
    with open('heart_disease_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Check if the model has a predict method
    if hasattr(model, 'predict'):
        # Sample input data for testing
        test_input = np.array([[50, 1, 1, 130, 250, 0, 1, 150, 0, 2.3, 0, 0, 3]])
        prediction = model.predict(test_input)
        print("Prediction:", prediction)
    else:
        print("The loaded object does not have a 'predict' method.")
except Exception as e:
    print(f"Error loading model: {e}")
