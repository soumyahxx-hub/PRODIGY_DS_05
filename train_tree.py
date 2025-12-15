# train_tree.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, accuracy_score, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import joblib
import sys

# 1. Load dataset
try:
    df = pd.read_csv("bank.csv", sep=";")  # Try semicolon (used in Bank Marketing dataset)
except FileNotFoundError:
    print("❌ bank.csv not found! Please place it in the same folder as this script.")
    sys.exit(1)

print("✅ Data loaded successfully. Shape:", df.shape)

# 2. Drop missing values if any
df = df.dropna()

# 3. Separate features (X) and target (y)
if 'y' not in df.columns:
    print("❌ Target column 'y' not found. Available columns:", df.columns.tolist())
    sys.exit(1)

X = df.drop(columns=['y'])
y = df['y'].map({'yes': 1, 'no': 0})  # Convert yes/no to 1/0

# 4. Identify categorical and numeric columns
cat_cols = X.select_dtypes(include=['object']).columns.tolist()
num_cols = X.select_dtypes(include=[np.number]).columns.tolist()
print(f"🧩 Categorical columns: {len(cat_cols)} | Numeric columns: {len(num_cols)}")

# 5. Preprocessing: encode categorical variables
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols)
    ],
    remainder='passthrough'
)

# 6. Split data into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 7. Transform and train model
X_train_t = preprocessor.fit_transform(X_train)
X_test_t = preprocessor.transform(X_test)

clf = DecisionTreeClassifier(max_depth=6, random_state=42)
clf.fit(X_train_t, y_train)

# 8. Evaluate model
y_pred = clf.predict(X_test_t)
acc = accuracy_score(y_test, y_pred)
print(f"\n🎯 Accuracy: {acc:.4f}")
print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred))

# 9. Confusion Matrix
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("Confusion Matrix")
plt.tight_layout()
plt.savefig("confusion_matrix.png")
print("📁 Saved confusion_matrix.png")

# 10. Decision Tree Visualization
plt.figure(figsize=(20, 10))
plot_tree(
    clf,
    filled=True,
    feature_names=list(preprocessor.named_transformers_['cat'].get_feature_names_out(cat_cols)) + num_cols,
    class_names=['no', 'yes'],
    rounded=True,
    fontsize=8
)
plt.tight_layout()
plt.savefig("decision_tree.png")
print("📁 Saved decision_tree.png")

# 11. Save trained model
joblib.dump({'preprocessor': preprocessor, 'model': clf}, "tree_pipeline.joblib")
print("✅ Model saved as tree_pipeline.joblib")
