# phishing_detector.py



import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv('phishing.csv')  # Make sure this filename matches your downloaded CSV
print(df.head())       # Shows the first 5 rows
print(df.shape)        # Shows (number of rows, number of columns)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load Dataset
data = pd.read_csv('phishing.csv')  # Rename to your actual CSV file
X = data.drop('Result', axis=1)
y = data['Result']

# Step 2: Split into training & testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train ML Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 4: Test model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
