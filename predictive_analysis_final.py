# -*- coding: utf-8 -*-
"""Predictive_analysis_FINAL.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1K7Nbwi1TOU2NU_5tLS8w7z1STYB9PIA7
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

df = pd.read_csv('/content/healthcare-dataset-stroke-data (1).csv')
df

# Convert categorical variables to numerical using LabelEncoder
categorical_cols = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
label_encoders = {}
for col in categorical_cols:
    label_encoders[col] = LabelEncoder()
    df[col] = label_encoders[col].fit_transform(df[col])

df

df.isnull()

#replace these null values with mean value ( avg ) of the column

#mean-value of bmi
mean = np.mean(df['bmi'])
mean

#use fillna to replace null-values

df['bmi'].fillna(mean,inplace=True)
df

##Normalization = 0-1 Range

from sklearn.preprocessing import MinMaxScaler

#make age,bmi,glucose-levels in 0-1 range

df[['gender','age','work_type','avg_glucose_level','bmi','smoking_status']] = MinMaxScaler().fit_transform(df[['gender','age','work_type','avg_glucose_level','bmi','smoking_status']])
df

# Split the data into features (X) and target variable (y)
X = df.drop('stroke', axis=1)
y = df['stroke']

"""# Unbalanced Data"""

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

"""Decision Tree Classifier"""

# Create a decision tree classifier
clf = DecisionTreeClassifier()

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Evaluate the accuracy of the classifier
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

"""# Support Vector Machine (SVM)"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Split the data into features (X) and target variable (y)
X = df.drop('stroke', axis=1)
y = df['stroke']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create an SVM classifier
clf = SVC()

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Calculate performance metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred)

# Print the performance metrics
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("Confusion Matrix:\n", confusion_mat)

"""Accuracy achieved using decision tree: 0.9060665362035225

Accuracy achieved using SVM: 0.9419439008480104

# Balancing the Data
"""

from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Perform SMOTE to balance the data
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Display the count of each class after balancing
class_counts = pd.Series(y_resampled).value_counts()
print("Class Counts after balancing:\n", class_counts)

# Split the resampled data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=42)

"""# Decision tree after balancing data"""

# Create a decision tree classifier
clf = DecisionTreeClassifier()

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Evaluate the accuracy of the classifier
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

"""# SVM after balancing data"""

# Create an SVM classifier
clf = SVC()

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

"""# Accuracy achieved after balancing and using Decision Tree: 0.8878600823045267

# Accuracy achieved after balancing and using SVM: 0.8240740740740741

# Confusion Matrix
"""

from sklearn.metrics import confusion_matrix

# Perform SMOTE to balance the data
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Split the resampled data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=42)

"""Decision tree"""

# Create a Decision Tree classifier
dt_clf = DecisionTreeClassifier()

# Train the Decision Tree classifier on the training data
dt_clf.fit(X_train, y_train)

# Make predictions on the test data using the Decision Tree classifier
dt_y_pred = dt_clf.predict(X_test)

# Generate the confusion matrix for Decision Tree classifier
dt_cm = confusion_matrix(y_test, dt_y_pred)
print("Decision Tree Confusion Matrix:\n", dt_cm)

"""Support Vector machine(SVM)"""

# Create an SVM classifier
svm_clf = SVC()

# Train the SVM classifier on the training data
svm_clf.fit(X_train, y_train)

# Make predictions on the test data using the SVM classifier
svm_y_pred = svm_clf.predict(X_test)

# Generate the confusion matrix for SVM classifier
svm_cm = confusion_matrix(y_test, svm_y_pred)
print("SVM Confusion Matrix:\n", svm_cm)

"""# ensemble learning

# Random Forest in balanced data
"""

# Perform SMOTE to balance the data
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Split the resampled data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=42)

# Create a Random Forest classifier
clf = RandomForestClassifier()

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Evaluate the accuracy of the classifier
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

"""# Adaboost Classifier"""

from sklearn.ensemble import AdaBoostClassifier

# Create an AdaBoost classifier
adaboost_clf = AdaBoostClassifier()

# Train the AdaBoost classifier on the training data
adaboost_clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = adaboost_clf.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

"""# Conclusion

Accuracy achieved using random forest: 0.9502743484224966

Accuracy achieved using AdaBoost: 0.8590534979423868

Among all the models, the Random Forest Classifier achieved the highest accuracy of 95% on the balanced data.
"""

