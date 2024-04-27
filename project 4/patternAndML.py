import numpy as np
import scipy.io
from collections import defaultdict
from scipy.stats import multivariate_normal
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

data = scipy.io.loadmat('project 4/Iris.mat')

labels = data['labels']
features = data['features']

indices = np.arange(features.shape[0])
np.random.shuffle(indices)
features = features[indices]
labels = labels[indices]

split_point = len(features) // 2
train_features = features[:split_point]
train_labels = labels[:split_point]
test_features = features[split_point:]
test_labels = labels[split_point:]

means = {}
covariances = {}


features_by_class = defaultdict(list)


for feature, label in zip(train_features, train_labels):
    features_by_class[label.item()].append(feature)  

for label in features_by_class:
    features_by_class[label] = np.array(features_by_class[label])

for label, feats in features_by_class.items():
    means[label] = np.mean(feats, axis=0)
    covariances[label] = np.cov(feats, rowvar=False)

for label in sorted(means):
    print(f"Class {label} Mean Vector:", means[label])
    print(f"Class {label} Covariance Matrix:\n", covariances[label])

def classify_sample(feature, means, covariances):
    max_likelihood = -np.inf
    best_class = None

    for label in means:
        likelihood = multivariate_normal.pdf(feature, mean=means[label], cov=covariances[label])
        if likelihood > max_likelihood:
            max_likelihood = likelihood
            best_class = label

    return best_class

predicted_labels = np.array([classify_sample(feature, means, covariances) for feature in test_features])

accuracy = np.mean(predicted_labels == test_labels)
print(f"Accuracy: {accuracy * 100:.2f}%")

cm = confusion_matrix(test_labels, predicted_labels)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=np.unique(train_labels), yticklabels=np.unique(train_labels))
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()

