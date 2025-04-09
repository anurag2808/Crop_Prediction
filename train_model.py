import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
file_path = 'data.csv'  # Make sure this file is in your project directory
data = pd.read_csv(file_path)

# Encode the target variable (label column)
le = LabelEncoder()
data['label'] = le.fit_transform(data['label'])

# Split features and target
X = data.drop(columns=['label'])
y = data['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
f1_rf = f1_score(y_test, y_pred_rf, average='macro')

print(f'Random Forest F1 Score: {f1_rf}')

# Save the model and label encoder
joblib.dump(rf_model, 'random_forest_model.pkl')
joblib.dump(le, 'label_encoder.pkl')