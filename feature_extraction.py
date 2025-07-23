import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Sample phishing dataset (you can expand this)
data = [
    # [url, label (1 = phishing, 0 = legitimate)]
    ("http://192.168.0.1/steal/login", 1),
    ("https://www.google.com", 0),
    ("http://bit.ly/fakebank", 1),
    ("https://www.github.com", 0),
    ("http://phishingsite.com/login@user", 1),
    ("https://openai.com", 0),
]

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

    features.extend([0] * (30 - len(features)))                    # Dummy fill to 30 features

    return features

# Create dataset
X = []
y = []

for url, label in data:
    feats = extract_features(url)
    X.append(feats)
    y.append(label)

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
