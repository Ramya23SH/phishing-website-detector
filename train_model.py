import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
from urllib.parse import urlparse
import re

def extract_features(url):
    features = []
    parsed = urlparse(url)

    features.append(len(url))                                      # 1. URL Length
    features.append(url.count('.'))                                # 2. Dot count
    features.append(1 if re.match(r'\d+\.\d+\.\d+\.\d+', parsed.netloc) else 0)  # 3. IP
    features.append(1 if '@' in url else 0)                        # 4. '@'
    features.append(1 if '-' in parsed.netloc else 0)             # 5. '-'
    features.append(len(parsed.netloc.split('.')) - 2)            # 6. Subdomains
    features.append(1 if parsed.scheme == 'https' else 0)         # 7. HTTPS

    features.extend([0] * (30 - len(features)))                    # Fill to 30 features

    return features

# ✅ Larger and balanced dataset
data = [
    # Phishing URLs
    ("http://192.168.0.1/steal/login", 1),
    ("http://bit.ly/paypal-login", 1),
    ("http://phishingsite.com/login@user", 1),
    ("http://secure-update-bank.com", 1),
    ("http://paypal-login.com", 1),
    ("http://free-prize-winner.com", 1),

    # Legitimate URLs
    ("https://www.google.com", 0),
    ("https://github.com", 0),
    ("https://www.bankofamerica.com", 0),
    ("https://accounts.google.com", 0),
    ("https://www.amazon.in", 0),
    ("https://openai.com", 0),
]

# Train
X = []
y = []

for url, label in data:
    X.append(extract_features(url))
    y.append(label)

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained on larger dataset and saved as model.pkl")
