import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Create a synthetic dataset for the computer-buying decision
data = [
    # budget, credit, age, student, decision (buy = 1, don't buy = 0)
    ['high', 'good', 'young', 'no', 1],        # Buy
    ['high', 'good', 'middle-aged', 'no', 1],  # Buy
    ['high', 'good', 'senior', 'no', 0],       # Don't Buy
    ['high', 'bad', 'young', 'yes', 1],        # Buy
    ['high', 'bad', 'young', 'no', 0],         # Don't Buy
    ['high', 'bad', 'middle-aged', 'no', 0],   # Don't Buy
    ['high', 'bad', 'middle-aged', 'yes', 0],  # Don't Buy
    ['high', 'bad', 'senior', 'no', 0],        # Don't Buy
    ['high', 'bad', 'senior', 'yes', 0],       # Don't Buy
    ['low', 'good', 'young', 'no', 1],         # Buy
    ['low', 'good', 'middle-aged', 'no', 0],   # Don't Buy
    ['low', 'good', 'senior', 'no', 0],        # Don't Buy
    ['low', 'bad', 'young', 'no', 0],          # Don't Buy
    ['low', 'bad', 'young', 'yes', 1],         # Buy
    ['low', 'bad', 'middle-aged', 'no', 0],    # Don't Buy
    ['low', 'bad', 'middle-aged', 'yes', 0],   # Don't Buy
    ['low', 'bad', 'senior', 'no', 0],         # Don't Buy
    ['low', 'bad', 'senior', 'yes', 0],        # Don't Buy
]

# Convert to numpy array
data = np.array(data)

# Extract features and labels
X = data[:, :-1]
y = data[:, -1].astype(int)

# Encode categorical features
le_budget = LabelEncoder()
le_credit = LabelEncoder()
le_age = LabelEncoder()
le_student = LabelEncoder()

X[:, 0] = le_budget.fit_transform(X[:, 0])
X[:, 1] = le_credit.fit_transform(X[:, 1])
X[:, 2] = le_age.fit_transform(X[:, 2])
X[:, 3] = le_student.fit_transform(X[:, 3])

# Convert features to float for compatibility
X = X.astype(float)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree classifier
clf = DecisionTreeClassifier(random_state=42)

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Display classification report and confusion matrix
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Visualize the decision tree
plt.figure(figsize=(20, 10))
plot_tree(clf, 
          feature_names=['Budget', 'Credit', 'Age', 'Student'], 
          class_names=['Don\'t Buy', 'Buy'], 
          filled=True, 
          rounded=True, 
          precision=2,
          fontsize=12)
plt.show()

# Decision-making function using the trained classifier
def decide_to_buy_computer(clf, budget, credit, age, student):
    # Encode user input using the LabelEncoders
    budget_encoded = le_budget.transform([budget])[0]
    credit_encoded = le_credit.transform([credit])[0]
    age_encoded = le_age.transform([age])[0]
    student_encoded = le_student.transform([student])[0]

    # Create feature array for prediction
    features = np.array([[budget_encoded, credit_encoded, age_encoded, student_encoded]])

    # Predict decision
    decision = clf.predict(features)
    return "Buy" if decision[0] == 1 else "Don't Buy"

# Example usage without manual input
decision = decide_to_buy_computer(clf, 'low', 'good', 'young', 'yes')
print("Decision:", decision)

# Uncomment to simulate manual input (will block in non-interactive environments)
# if _name_ == "_main_":
#     print("Enter the attributes to decide whether to buy a computer or not:")
#     budget = input("Enter your budget (high/low): ").lower()
#     credit = input("Enter your credit status (good/bad): ").lower()
#     age = input("Enter your age (young/middle-aged/senior): ").lower()
#     student = input("Are you a student? (yes/no): ").lower()
#     decision = decide_to_buy_computer(clf, budget, credit, age, student)
#     print("Decision:", decision)