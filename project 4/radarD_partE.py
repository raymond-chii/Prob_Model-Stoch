import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


def getThreshold(A, sigma, P_present, P_absent):
    return (sigma**2 / A) * np.log(P_absent / P_present) + A/2

def simulateRadarDetection(N, A, sigma, sigma_z, threshold, P_present, P_absent):
    errors = 0
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for _ in range(N):
        present = np.random.rand() < P_present
        X = np.random.normal(0, sigma)
        Z = np.random.normal(0, sigma_z)
        Y = A + X if present else A + Z  
        detected_present = Y > threshold
        if detected_present:
            if present:
                TP += 1
            else:
                FP += 1
                errors += 1
        else:
            if present:
                FN += 1
                errors += 1
            else:
                TN += 1
    TPR = TP / (TP + FN) if TP + FN > 0 else 0
    FPR = FP / (FP + TN) if FP + TN > 0 else 0
    return TPR, FPR

def plotROC(A, sigma, sigma_z_ratios, numOfSamples):
    plt.figure(figsize=(10, 8))
    for sigma_z_ratio in sigma_z_ratios:
        sigma_z = sigma * np.sqrt(sigma_z_ratio)  # Calculate σ_z based on the ratio
        threshold = getThreshold(A, sigma, P_present, P_absent)
        TPRs, FPRs = [], []
        for thresh in np.linspace(threshold - 3, threshold + 3, 100):
            TPR, FPR = simulateRadarDetection(numOfSamples, A, sigma, sigma_z, thresh, P_present, P_absent)
            TPRs.append(TPR)
            FPRs.append(FPR)
        plt.plot(FPRs, TPRs, label=f'σ²_z/σ² = {sigma_z_ratio}')
    plt.title('ROC Curve for Different Ratios of σ²_z to σ²')
    plt.xlabel('False Positive Rate (FPR)')
    plt.ylabel('True Positive Rate (TPR)')
    plt.legend()
    plt.grid(True)
    plt.show()


A = 1
sigma = 1
P_present = 0.2
P_absent = 0.8
numOfSamples = 1000
sigma_z_ratios = [1, 2, 5, 10] 

plotROC(A, sigma, sigma_z_ratios, numOfSamples)
