import os
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

os.system("cls")

# Nilai-nilai sebenarnya
actual = [1, 0, 1, 0, 1, 1, 0, 1, 0, 0]
# Nilai-nilai hasil prediksi
# predicted = [0, 0, 1, 0, 1, 0, 1, 1, 0, 1]
predicted = [1, 0, 1, 0, 1, 1, 0, 1, 0, 0]

# Menghitung confusion matrix
cm = confusion_matrix(actual, predicted)
print("Nilai Confusion Matrix adalah :")
print(cm)

# Calculate performance parameters
accuracy = accuracy_score(actual, predicted)
precision = precision_score(actual, predicted)
recall = recall_score(actual, predicted)
f1 = f1_score(actual, predicted)

print("\nRangkuman Performance Parameters:")
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
