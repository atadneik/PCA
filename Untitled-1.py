# ============================================================
# PCA ON WINE DATASET
# Unsupervised Learning - Principal Component Analysis
# Complete Code with Train/Test Split, Baseline, Evaluation Metrics
# ============================================================

# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import cross_val_score, StratifiedKFold

import seaborn as sns
from scipy import stats


# ============================================================
# 2. LOAD DATASET
# ============================================================

df = pd.read_csv("Wine dataset.csv")

# Clean column names: remove extra spaces
df.columns = df.columns.str.strip()

print("===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET INFORMATION =====")
print(df.info())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())


# ============================================================
# 3. DATA CLEANING
# ============================================================

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATED ROWS =====")
print("Number of duplicated rows:", df.duplicated().sum())

# Remove duplicated rows if any
df = df.drop_duplicates()

print("\nDataset shape after cleaning:", df.shape)


# ============================================================
# 4. SEPARATE FEATURES AND LABEL
# ============================================================

# PCA does not use the class label for training.
# The class label is used only for stratified splitting, visualization,
# and additional classification evaluation.
X = df.drop("class", axis=1)
y = df["class"]

print("\n===== PCA INPUT FEATURES =====")
print(X.columns.tolist())

print("\nNumber of samples:", X.shape[0])
print("Number of original features:", X.shape[1])


# ============================================================
# 4b. ENHANCED EDA – CORRELATION, DISTRIBUTION, OUTLIER
# ============================================================

# Correlation Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(X.corr(), annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Correlation Heatmap of Wine Features")
plt.tight_layout()
plt.show()

# Distribution of each feature
X.hist(bins=20, figsize=(15, 10))
plt.suptitle("Feature Distributions")
plt.tight_layout()
plt.show()

# Boxplot to detect outliers
plt.figure(figsize=(15, 6))
X.boxplot(rot=45)
plt.title("Boxplot of Wine Features")
plt.tight_layout()
plt.show()

print("\n===== ENHANCED EDA COMPLETED =====")


# ============================================================
# 5. TRAIN / TEST SPLIT - STRATIFIED RANDOM SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\n===== TRAIN / TEST SPLIT =====")
print("Training set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)

print("\nOriginal class distribution:")
print(y.value_counts(normalize=True))

print("\nTraining class distribution:")
print(y_train.value_counts(normalize=True))

print("\nTesting class distribution:")
print(y_test.value_counts(normalize=True))


# ============================================================
# 6. STANDARDIZATION
# ============================================================

# Fit StandardScaler only on training data to avoid data leakage
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\n===== STANDARDIZATION COMPLETED =====")
print("Mean of scaled training data:", np.round(X_train_scaled.mean(), 4))
print("Standard deviation of scaled training data:", np.round(X_train_scaled.std(), 4))


# ============================================================
# 7. BASELINE SETUP
# ============================================================

# Baseline = original standardized data with all 13 features
print("\n===== BASELINE INFORMATION =====")
print("Baseline data: Original standardized Wine dataset")
print("Original number of features:", X_train_scaled.shape[1])
print("Training samples:", X_train_scaled.shape[0])
print("Testing samples:", X_test_scaled.shape[0])


# ============================================================
# 8. BASELINE CLASSIFIER USING ORIGINAL FEATURES
# ============================================================

# This is an additional evaluation.
# Accuracy is not the main metric of PCA.
baseline_model = LogisticRegression(max_iter=1000, random_state=42)
baseline_model.fit(X_train_scaled, y_train)

y_pred_baseline = baseline_model.predict(X_test_scaled)
baseline_accuracy = accuracy_score(y_test, y_pred_baseline)

print("\n===== BASELINE CLASSIFIER RESULT =====")
print("Model: Logistic Regression")
print("Input: Original 13 standardized features")
print("Baseline accuracy:", baseline_accuracy)

print("\nClassification report:")
print(classification_report(y_test, y_pred_baseline))


# ============================================================
# 9. APPLY PCA WITH 2 COMPONENTS
# ============================================================

# PCA is fitted only on the training set to avoid data leakage
pca = PCA(n_components=2)

X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

print("\n===== PCA RESULT =====")
print("Training PCA shape:", X_train_pca.shape)
print("Testing PCA shape:", X_test_pca.shape)


# ============================================================
# 10. PCA EVALUATION METRICS
# ============================================================

# Explained Variance Ratio
pc1_variance = pca.explained_variance_ratio_[0]
pc2_variance = pca.explained_variance_ratio_[1]
total_explained_variance = pca.explained_variance_ratio_.sum()

# Number of features before and after PCA
original_features = X_train_scaled.shape[1]
pca_components = X_train_pca.shape[1]

# Dimensionality Reduction Ratio
dimensionality_reduction_ratio = (1 - pca_components / original_features) * 100

# Information Loss
information_loss = (1 - total_explained_variance) * 100

print("\n===== PCA EVALUATION METRICS =====")
print("Original number of features:", original_features)
print("Number of PCA components:", pca_components)

print("\nExplained Variance Ratio:")
print("PC1 explained variance:", pc1_variance)
print("PC2 explained variance:", pc2_variance)
print("Total explained variance retained:", total_explained_variance)

print("\nDimensionality reduction ratio:", dimensionality_reduction_ratio, "%")
print("Information loss:", information_loss, "%")


# ============================================================
# 11. RECONSTRUCTION ERROR
# ============================================================

# Reconstruct the standardized data from PCA components
X_train_reconstructed = pca.inverse_transform(X_train_pca)
X_test_reconstructed = pca.inverse_transform(X_test_pca)

# Calculate reconstruction error
train_reconstruction_error = np.mean((X_train_scaled - X_train_reconstructed) ** 2)
test_reconstruction_error = np.mean((X_test_scaled - X_test_reconstructed) ** 2)

print("\n===== RECONSTRUCTION ERROR =====")
print("Training reconstruction error:", train_reconstruction_error)
print("Testing reconstruction error:", test_reconstruction_error)


# ============================================================
# 12. PCA RESULT COMPARED TO BASELINE
# ============================================================

print("\n===== PCA RESULT COMPARED TO BASELINE =====")
print("Original data:", original_features, "features")
print("PCA data:", pca_components, "principal components")
print("Dimensionality reduction:", original_features, "features ->", pca_components, "principal components")
print("Total explained variance retained:", total_explained_variance)
print("Information loss:", information_loss, "%")


# ============================================================
# 13. CREATE PCA OUTPUT DATAFRAME
# ============================================================

train_pca_df = pd.DataFrame(
    X_train_pca,
    columns=["PC1", "PC2"]
)
train_pca_df["class"] = y_train.values
train_pca_df["set"] = "train"

test_pca_df = pd.DataFrame(
    X_test_pca,
    columns=["PC1", "PC2"]
)
test_pca_df["class"] = y_test.values
test_pca_df["set"] = "test"

pca_result_df = pd.concat([train_pca_df, test_pca_df], ignore_index=True)

print("\n===== PCA OUTPUT DATA =====")
print(pca_result_df.head())


# ============================================================
# 14. PCA VISUALIZATION
# ============================================================

plt.figure(figsize=(8, 6))

for wine_class in sorted(pca_result_df["class"].unique()):
    subset = pca_result_df[pca_result_df["class"] == wine_class]
    plt.scatter(
        subset["PC1"],
        subset["PC2"],
        label=f"Class {wine_class}",
        alpha=0.8
    )

plt.title("PCA Visualization of Wine Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.grid(True)
plt.show()


# ============================================================
# 15. SCREE PLOT AND CUMULATIVE EXPLAINED VARIANCE
# ============================================================

# Fit PCA with all components to analyze variance
pca_full = PCA()
pca_full.fit(X_train_scaled)

explained_variance = pca_full.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)

print("\n===== EXPLAINED VARIANCE FOR ALL COMPONENTS =====")
for i, variance in enumerate(explained_variance):
    print(f"PC{i + 1}: {variance:.4f}")

print("\n===== CUMULATIVE EXPLAINED VARIANCE =====")
for i, variance in enumerate(cumulative_variance):
    print(f"{i + 1} components: {variance:.4f}")


# Scree Plot
plt.figure(figsize=(8, 5))
plt.plot(
    range(1, len(explained_variance) + 1),
    explained_variance,
    marker="o"
)

plt.title("Scree Plot")
plt.xlabel("Principal Component")
plt.ylabel("Explained Variance Ratio")
plt.grid(True)
plt.show()


# Cumulative Explained Variance Plot
plt.figure(figsize=(8, 5))
plt.plot(
    range(1, len(cumulative_variance) + 1),
    cumulative_variance,
    marker="o"
)

plt.axhline(y=0.95, linestyle="--", label="95% variance threshold")
plt.title("Cumulative Explained Variance")
plt.xlabel("Number of Principal Components")
plt.ylabel("Cumulative Explained Variance")
plt.legend()
plt.grid(True)
plt.show()


# ============================================================
# 15b. MODEL INTERPRETABILITY – FEATURE LOADINGS & BIPLOT
# ============================================================

# Feature loadings: contribution of each original feature to each PC
feature_names = X.columns.tolist()
loadings = pca.components_   # shape: (n_components, n_features)

loadings_df = pd.DataFrame(
    loadings.T,
    columns=[f"PC{i+1}" for i in range(loadings.shape[0])],
    index=feature_names
)
print("\n===== FEATURE LOADINGS (PC1 & PC2) =====")
print(loadings_df.round(4))

# Bar chart of loadings
loadings_df.plot(kind="bar", figsize=(12, 5))
plt.title("Feature Loadings on PC1 & PC2")
plt.ylabel("Loading Value")
plt.xticks(rotation=45, ha="right")
plt.axhline(0, color="black", linewidth=0.8)
plt.tight_layout()
plt.show()

# Biplot: scatter + loading arrows
fig, ax = plt.subplots(figsize=(10, 7))
for wine_class in sorted(pca_result_df["class"].unique()):
    subset = pca_result_df[pca_result_df["class"] == wine_class]
    ax.scatter(subset["PC1"], subset["PC2"], label=f"Class {wine_class}", alpha=0.7)

arrow_scale = 3
for i, feat in enumerate(feature_names):
    ax.arrow(0, 0,
             loadings[0, i] * arrow_scale,
             loadings[1, i] * arrow_scale,
             head_width=0.05, head_length=0.05, fc="red", ec="red")
    ax.text(loadings[0, i] * arrow_scale * 1.12,
            loadings[1, i] * arrow_scale * 1.12,
            feat, fontsize=8, color="red")

ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_title("Biplot – PCA Wine Dataset")
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.show()

print("\n===== MODEL INTERPRETABILITY COMPLETED =====")


# ============================================================
# 16. PCA HYPERPARAMETER TUNING
# ============================================================

# Main PCA hyperparameter: n_components
# Find how many components are needed to retain 95% variance
pca_95 = PCA(n_components=0.95)

X_train_pca_95 = pca_95.fit_transform(X_train_scaled)
X_test_pca_95 = pca_95.transform(X_test_scaled)

print("\n===== PCA HYPERPARAMETER TUNING =====")
print("Hyperparameter: n_components")
print("Number of components needed to retain 95% variance:", pca_95.n_components_)
print("Total variance retained:", np.sum(pca_95.explained_variance_ratio_))


# ============================================================
# 16b. CROSS VALIDATION (GROSS VALIDATION)
# ============================================================

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# CV on baseline (13 original features)
baseline_cv_scores = cross_val_score(
    LogisticRegression(max_iter=1000, random_state=42),
    X_train_scaled, y_train, cv=cv, scoring="accuracy"
)

# CV on PCA-reduced data (2 components)
pca_cv_scores = cross_val_score(
    LogisticRegression(max_iter=1000, random_state=42),
    X_train_pca, y_train, cv=cv, scoring="accuracy"
)

print("\n===== CROSS VALIDATION (5-Fold StratifiedKFold) =====")
print("Baseline CV scores:", np.round(baseline_cv_scores, 4))
print(f"Baseline CV mean ± std: {baseline_cv_scores.mean():.4f} ± {baseline_cv_scores.std():.4f}")

print("\nPCA CV scores:", np.round(pca_cv_scores, 4))
print(f"PCA CV mean ± std: {pca_cv_scores.mean():.4f} ± {pca_cv_scores.std():.4f}")

# Visualize CV results
fig, ax = plt.subplots(figsize=(8, 5))
ax.boxplot([baseline_cv_scores, pca_cv_scores], labels=["Baseline (13 features)", "PCA (2 components)"])
ax.set_title("Cross Validation Accuracy – Baseline vs PCA")
ax.set_ylabel("Accuracy")
ax.grid(True, axis="y")
plt.tight_layout()
plt.show()


# ============================================================
# 16c. EXPERIMENT MANAGEMENT – n_components SWEEP
# ============================================================

experiment_results = []
for n in range(1, X_train_scaled.shape[1] + 1):
    pca_exp = PCA(n_components=n)
    X_tr_exp = pca_exp.fit_transform(X_train_scaled)
    X_te_exp = pca_exp.transform(X_test_scaled)
    clf_exp = LogisticRegression(max_iter=1000, random_state=42)
    clf_exp.fit(X_tr_exp, y_train)
    acc_exp = accuracy_score(y_test, clf_exp.predict(X_te_exp))
    var_exp = pca_exp.explained_variance_ratio_.sum()
    experiment_results.append({
        "n_components": n,
        "accuracy": acc_exp,
        "explained_variance": var_exp
    })

experiment_df = pd.DataFrame(experiment_results)
print("\n===== EXPERIMENT MANAGEMENT – n_components SWEEP =====")
print(experiment_df.to_string(index=False))
experiment_df.to_csv("experiment_results.csv", index=False)

fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.plot(experiment_df["n_components"], experiment_df["accuracy"], "b-o", label="Accuracy")
ax1.set_xlabel("n_components")
ax1.set_ylabel("Accuracy", color="b")
ax1.tick_params(axis="y", labelcolor="b")
ax2 = ax1.twinx()
ax2.plot(experiment_df["n_components"], experiment_df["explained_variance"], "r--s", label="Explained Variance")
ax2.set_ylabel("Explained Variance", color="r")
ax2.tick_params(axis="y", labelcolor="r")
plt.title("Experiment: n_components vs Accuracy & Explained Variance")
fig.tight_layout()
plt.show()

print("Experiment results saved to 'experiment_results.csv'.")


# ============================================================
# 17. CLASSIFIER USING PCA-REDUCED DATA
# ============================================================

# This is additional evaluation only.
# PCA itself is not a classification algorithm.
pca_classifier = LogisticRegression(max_iter=1000, random_state=42)
pca_classifier.fit(X_train_pca, y_train)

y_pred_pca = pca_classifier.predict(X_test_pca)
pca_accuracy = accuracy_score(y_test, y_pred_pca)

print("\n===== PCA CLASSIFIER RESULT =====")
print("Model: Logistic Regression")
print("Input: 2 PCA components")
print("PCA-based classifier accuracy:", pca_accuracy)

print("\nClassification report:")
print(classification_report(y_test, y_pred_pca))


# ============================================================
# 17b. ERROR ANALYSIS – CONFUSION MATRIX & MISCLASSIFIED SAMPLES
# ============================================================

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred_pca)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=sorted(y_test.unique()))
fig, ax = plt.subplots(figsize=(6, 5))
disp.plot(cmap="Blues", ax=ax)
plt.title("Confusion Matrix – PCA Classifier (2 components)")
plt.tight_layout()
plt.show()

# Misclassified sample analysis
misclassified_idx = np.where(y_pred_pca != y_test.values)[0]
print("\n===== ERROR ANALYSIS =====")
print(f"Total test samples: {len(y_test)}")
print(f"Number of misclassified samples: {len(misclassified_idx)}")
print(f"Error rate: {len(misclassified_idx)/len(y_test)*100:.2f}%")

if len(misclassified_idx) > 0:
    print("\nMisclassified samples (PC1, PC2, True Label, Predicted):")
    for idx in misclassified_idx:
        print(f"  PC1={X_test_pca[idx, 0]:.3f}, PC2={X_test_pca[idx, 1]:.3f}, "
              f"True={y_test.values[idx]}, Predicted={y_pred_pca[idx]}")


# ============================================================
# 17c. STATISTICAL VALIDATION
# ============================================================

# Paired t-test between Baseline CV scores and PCA CV scores
t_stat, p_value = stats.ttest_rel(baseline_cv_scores, pca_cv_scores)

print("\n===== STATISTICAL VALIDATION =====")
print(f"Paired t-test (Baseline vs PCA):")
print(f"  t-statistic = {t_stat:.4f}")
print(f"  p-value     = {p_value:.4f}")

if p_value < 0.05:
    print("  => Có sự khác biệt có ý nghĩa thống kê (p < 0.05)")
else:
    print("  => Không có sự khác biệt có ý nghĩa thống kê (p >= 0.05)")

# 95% Confidence Interval for PCA CV accuracy
ci = stats.t.interval(
    0.95,
    df=len(pca_cv_scores) - 1,
    loc=pca_cv_scores.mean(),
    scale=stats.sem(pca_cv_scores)
)
print(f"\n95% Confidence Interval for PCA CV accuracy: [{ci[0]:.4f}, {ci[1]:.4f}]")

# 95% Confidence Interval for Baseline CV accuracy
ci_baseline = stats.t.interval(
    0.95,
    df=len(baseline_cv_scores) - 1,
    loc=baseline_cv_scores.mean(),
    scale=stats.sem(baseline_cv_scores)
)
print(f"95% Confidence Interval for Baseline CV accuracy: [{ci_baseline[0]:.4f}, {ci_baseline[1]:.4f}]")


# ============================================================
# 18. FINAL COMPARISON
# ============================================================

print("\n===== FINAL COMPARISON =====")
print("Baseline accuracy using original 13 features:", baseline_accuracy)
print("Accuracy using 2 PCA components:", pca_accuracy)
print("Accuracy difference:", baseline_accuracy - pca_accuracy)

if pca_accuracy > baseline_accuracy:
    print("Result: PCA-reduced data exceeds the baseline accuracy.")
elif pca_accuracy == baseline_accuracy:
    print("Result: PCA-reduced data achieves the same accuracy as the baseline.")
else:
    print("Result: PCA-reduced data does not exceed the baseline accuracy.")
    print("However, this can still be acceptable because PCA reduces dimensionality from 13 features to 2 components.")


# ============================================================
# 19. SAVE OUTPUT
# ============================================================

pca_result_df.to_csv("pca_wine_output.csv", index=False)

print("\n===== SAVED OUTPUT =====")
print("PCA result has been saved to 'pca_wine_output.csv'.")