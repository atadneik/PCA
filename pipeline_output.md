# 📊 Kết Quả Pipeline PCA – Wine Dataset

> **Dataset**: UCI Wine Recognition | 178 mẫu · 13 đặc trưng · 3 lớp  
> **Mục tiêu**: Giảm chiều dữ liệu từ 13 features → 2 principal components bằng PCA

---

## Bước 1 – EDA (Exploratory Data Analysis)

### 1a. Thông tin cơ bản

```
Shape: (178, 14)   ← 178 mẫu, 13 features + 1 cột class
```

**5 dòng đầu tiên:**

| class | Alcohol | Malic acid | Ash | Alcalinity | Magnesium | ... | Proline |
|-------|---------|------------|-----|------------|-----------|-----|---------|
| 1 | 14.23 | 1.71 | 2.43 | 15.6 | 127 | ... | 1065 |
| 1 | 13.20 | 1.78 | 2.14 | 11.2 | 100 | ... | 1050 |
| 1 | 13.16 | 2.36 | 2.67 | 18.6 | 101 | ... | 1185 |
| 1 | 14.37 | 1.95 | 2.50 | 16.8 | 113 | ... | 1480 |
| 1 | 13.24 | 2.59 | 2.87 | 21.0 | 118 | ... | 735  |

**Thống kê mô tả:**

| | Alcohol | Malic acid | Ash | Magnesium | Flavanoids | Proline |
|---|---|---|---|---|---|---|
| mean | 13.00 | 2.34 | 2.37 | 99.74 | 2.03 | 746.89 |
| std  | 0.81  | 1.12 | 0.27 | 14.28 | 1.00  | 314.91 |
| min  | 11.03 | 0.74 | 1.36 | 70.00 | 0.34  | 278.00 |
| max  | 14.83 | 5.80 | 3.23 | 162.00| 5.08  | 1680.00|

### 1b. Phân phối lớp

```
Class 2: 71 mẫu  (39.9%)
Class 1: 59 mẫu  (33.1%)
Class 3: 48 mẫu  (27.0%)
```

### 1c. Top 5 cặp features tương quan cao nhất

```
Total phenols  <-> Flavanoids                   :  0.865  ← rất cao
Flavanoids     <-> OD280/OD315 of diluted wines :  0.787
Total phenols  <-> OD280/OD315 of diluted wines :  0.700
Flavanoids     <-> Proanthocyanins              :  0.653
Alcohol        <-> Proline                      :  0.644
```

> 💡 **Nhận xét**: Nhiều features tương quan cao → PCA phù hợp để loại bỏ redundancy.

### 1d. Biểu đồ xuất ra
- 🗺️ **Correlation Heatmap** – ma trận tương quan 13×13 với màu đỏ/xanh
- 📊 **Feature Distributions** – 13 histogram phân phối từng biến
- 📦 **Boxplot** – phát hiện outlier theo từng feature

---

## Bước 2 – Data Cleaning

```
Missing values: 0 (tất cả 14 cột đều không có giá trị thiếu)
Duplicated rows: 0
Dataset shape sau cleaning: (178, 14)  ← không thay đổi
```

> ✅ **Kết quả**: Dữ liệu sạch, không cần xử lý thêm.

---

## Bước 3 – Feature Engineering (Standardization)

> StandardScaler được fit **chỉ trên tập train** để tránh data leakage.

```
Mean của scaled train data : -0.000000  (≈ 0)
Std  của scaled train data :  1.000000  (= 1)
```

**13 features đầu vào PCA:**
```
['Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium',
 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']
```

---

## Bước 4 – Data Split

```
Chiến lược: Stratified Random Split (80% train / 20% test)

Train set: (142, 13)
Test  set: ( 36, 13)

Phân phối class trong train:
  Class 2: 57 mẫu
  Class 1: 47 mẫu
  Class 3: 38 mẫu

Phân phối class trong test:
  Class 2: 14 mẫu
  Class 1: 12 mẫu
  Class 3: 10 mẫu
```

> ✅ **Stratified** đảm bảo tỷ lệ lớp được giữ nguyên trong cả train và test.

---

## Bước 5 – Baseline Model

> **Model**: Logistic Regression trên **13 features gốc** (sau chuẩn hóa)

```
Baseline Accuracy: 0.9722  (97.22%)

Classification Report:
              precision  recall  f1-score  support
Class 1          1.00    1.00      1.00      12
Class 2          0.93    1.00      0.97      14
Class 3          1.00    0.90      0.95      10

accuracy                           0.97      36
```

> 🎯 **Đây là ngưỡng tham chiếu**: accuracy **97.22%** với đầy đủ 13 features.

---

## Bước 6 – Model Selection (Chọn n_components = 2)

> PCA với **2 thành phần chính** được chọn để trực quan hóa 2D.

```
Train PCA shape: (142, 2)
Test  PCA shape: ( 36, 2)
```

### Biểu đồ PCA Visualization
- 🔵🟠🟢 Scatter plot 2D – 3 lớp phân tách khá rõ theo PC1 và PC2

---

## Bước 7 – Hyperparameter Tuning

> **Câu hỏi**: Cần bao nhiêu components để giữ ≥ 95% thông tin?

```
PCA(n_components=0.95) → tự động chọn số components tối thiểu

Kết quả: Cần 10 components để giữ 96.24% variance
```

### Scree Plot & Cumulative Explained Variance

| PC | Variance | Cumulative | Ghi chú |
|----|----------|------------|---------|
| PC1  | 35.79% | 35.79%  | Lớn nhất |
| PC2  | 19.27% | **55.06%** | ← 2 PC giữ 55% |
| PC3  | 11.02% | 66.08%  | |
| PC4  | 7.27%  | 73.35%  | |
| PC5  | 6.72%  | 80.08%  | |
| PC6  | 5.13%  | 85.21%  | |
| PC7  | 4.38%  | 89.59%  | |
| PC8  | 2.50%  | 92.09%  | |
| PC9  | 2.28%  | 94.37%  | |
| **PC10** | **1.88%** | **96.24%** | ← đạt 95% |
| PC11 | 1.78%  | 98.03%  | |
| PC12 | 1.26%  | 99.28%  | |
| PC13 | 0.72%  | 100.00% | |

> 📈 **Scree Plot** – đường gấp khúc giảm dần, "elbow" tại PC3-4  
> 📈 **Cumulative Variance Plot** – đường cong với ngưỡng 95% (nét đứt đỏ)

---

## Bước 8 – Train Model (PCA fit + transform)

```
PCA(n_components=2) fit ONLY trên X_train → tránh data leakage

PC1 Explained Variance:  35.79%
PC2 Explained Variance:  19.27%
Total Variance Retained: 55.06%
```

---

## Bước 9 – Evaluation Metrics (PCA)

```
Số features gốc    : 13
Số PCA components  : 2

Dimensionality Reduction Ratio : 84.62%
                                 (từ 13 features → 2 components)

Total Explained Variance       : 55.06%
Information Loss               : 44.94%

Reconstruction Error (MSE):
  Train: 0.4494
  Test : 0.4732
```

> 💡 **Nhận xét**: Giảm 84.62% số chiều nhưng mất 44.94% thông tin.  
> Đây là trade-off của việc chỉ dùng 2 components.  
> Nếu cần accuracy cao hơn → chọn n=3 hoặc n=10 (xem Experiment Management).

---

## Bước 10 – Cross Validation (5-Fold Stratified)

```
Fold              :    1       2       3       4       5
Baseline (13 feat): 0.9310  1.0000  1.0000  1.0000  0.9643
PCA (2 comp)      : 0.8966  1.0000  1.0000  0.9643  0.9643

Baseline CV: mean = 0.9791  std = 0.0277
PCA CV     : mean = 0.9650  std = 0.0378
```

> 📊 **Boxplot CV** – so sánh độ phân tán accuracy Baseline vs PCA  
> 💡 PCA kém hơn ~1.4% nhưng đổi lấy 84.62% giảm chiều.

---

## Bước 11 – Experiment Management (n_components sweep)

> Vòng lặp thử từ n=1 đến n=13, ghi lại accuracy + explained variance.  
> Kết quả lưu tại: `experiment_results.csv`

| n_components | Accuracy | Explained Variance | Ghi chú |
|:---:|:---:|:---:|---|
| 1  | 88.89% | 35.79% | |
| **2**  | 91.67% | 55.06% | ← được chọn (visualize 2D) |
| **3**  | **100.00%** | 66.08% | ← **Best accuracy!** |
| 4  | 100.00% | 73.35% | = n=3 nhưng nhiều chiều hơn |
| 5  | 97.22% | 80.08% | |
| 6–12 | 97.22% | ... | ổn định |
| 13 | 97.22% | 100.00% | = baseline |

> 📈 **Dual-axis chart**: accuracy (xanh, trái) và explained variance (đỏ, phải)  
> 💡 **Sweet spot**: **n=3** cho accuracy 100% với chỉ 66.08% variance!

---

## Bước 12 – Statistical Validation

```
Paired t-test (Baseline CV vs PCA CV):
  t-statistic  =  1.6326
  p-value      =  0.1779

  => Không có sự khác biệt có ý nghĩa thống kê (p = 0.18 >= 0.05)

95% Confidence Interval:
  PCA Accuracy      : [0.9126,  1.0175]
  Baseline Accuracy : [0.9406,  1.0175]
```

> ✅ **Kết luận**: Mặc dù PCA accuracy thấp hơn baseline ~1.4%, sự khác biệt này  
> **không có ý nghĩa thống kê** (p=0.18 > 0.05). Hai CI chồng lấp nhau nhiều.  
> PCA vẫn là lựa chọn hợp lý vì giảm chiều đáng kể mà không ảnh hưởng thực sự.

---

## Bước 13 – Error Analysis

### PCA Classifier (2 components)

```
Accuracy: 0.9167  (91.67%)

              precision  recall  f1-score  support
Class 1          0.92    0.92      0.92      12
Class 2          0.87    0.93      0.90      14
Class 3          1.00    0.90      0.95      10

accuracy                           0.92      36
```

### Confusion Matrix

```
              Predicted
              Class 1  Class 2  Class 3
Actual  1   [  11        1        0  ]  ← 1 bị nhầm sang Class 2
Actual  2   [   1       13        0  ]  ← 1 bị nhầm sang Class 1
Actual  3   [   0        1        9  ]  ← 1 bị nhầm sang Class 2
```

> 🔲 **Confusion Matrix heatmap** (màu xanh đậm nhạt theo số lượng)

### 3 mẫu bị phân loại sai (3/36 = 8.33%)

| # | PC1 | PC2 | True Label | Predicted | Lý do |
|---|-----|-----|-----------|-----------|-------|
| 1 | -2.427 | -0.369 | Class 3 | Class 2 | Nằm vùng chồng lấp 3-2 |
| 2 |  1.566 |  0.158 | Class 2 | Class 1 | Nằm vùng chồng lấp 2-1 |
| 3 |  1.570 | -0.691 | Class 1 | Class 2 | Nằm vùng chồng lấp 1-2 |

> 💡 **Nhận xét**: Cả 3 mẫu sai đều ở **vùng ranh giới** giữa các lớp.  
> Khi nén từ 13D → 2D, ranh giới quyết định kém rõ ràng hơn – điều này hoàn toàn bình thường.

---

## Bước 14 – Model Interpretability

### Feature Loadings (đóng góp vào PC1 và PC2)

| Feature | PC1 | PC2 | Vai trò |
|---|:---:|:---:|---|
| Flavanoids | **+0.4295** | -0.0025 | Đóng góp lớn nhất cho PC1 |
| Total phenols | **+0.3944** | +0.0763 | Đóng góp lớn cho PC1 |
| OD280/OD315 | **+0.3832** | -0.1703 | Đóng góp lớn cho PC1 |
| Proanthocyanins | **+0.3133** | +0.0109 | Đóng góp cho PC1 |
| Color intensity | -0.0964 | **+0.5244** | Đóng góp lớn nhất cho PC2 |
| Alcohol | +0.1444 | **+0.4869** | Đóng góp lớn cho PC2 |
| Proline | +0.2899 | **+0.3575** | Đóng góp cho PC2 |
| Nonflavanoid | **-0.2914** | +0.0208 | Kéo PC1 xuống (âm) |
| Malic acid | -0.2337 | +0.2229 | Kéo PC1 xuống (âm) |

### Giải thích ý nghĩa PC1 và PC2

```
PC1 (35.79% variance):
  → Đại diện cho nhóm "Phenolic compounds"
  → Cao khi: Flavanoids, Total phenols, OD280/OD315 cao
  → Thấp khi: Nonflavanoid phenols, Malic acid cao

PC2 (19.27% variance):
  → Đại diện cho nhóm "Color & Alcohol"
  → Cao khi: Color intensity và Alcohol cao
```

### Biểu đồ xuất ra
> 📊 **Loading bar chart** – 13 features so sánh loading trên PC1 và PC2  
> 🔀 **Biplot** – điểm scatter 3 lớp + 13 mũi tên đỏ (loading vectors)  
> &nbsp;&nbsp;&nbsp;&nbsp; Mũi tên dài = feature ảnh hưởng nhiều đến trục PC đó

---

## Tổng kết So sánh

| Chỉ số | Baseline (13 features) | PCA (2 components) |
|---|:---:|:---:|
| Test Accuracy | **97.22%** | 91.67% |
| CV Mean Accuracy | **97.91%** | 96.50% |
| CV Std | 0.0277 | 0.0378 |
| Số features | 13 | **2** |
| Variance giữ lại | 100% | 55.06% |
| Giảm chiều | – | **84.62%** |
| p-value (t-test) | – | 0.18 *(không có ý nghĩa)* |

### Kết luận cuối

```
Baseline accuracy  :  97.22%
PCA (n=2) accuracy :  91.67%
Chênh lệch         :   5.56%
p-value            :   0.18  → không có ý nghĩa thống kê

Khuyến nghị:
  ✅ Visualize 2D        → dùng n=2
  ✅ Maximize accuracy   → dùng n=3  (100% accuracy, 66% variance)
  ✅ Giữ 95% thông tin   → dùng n=10 (96.24% variance)
```

---

*📁 Output files:*  
*&nbsp;&nbsp;&nbsp;&nbsp;`pca_wine_output.csv` – kết quả PCA (PC1, PC2, class, set)*  
*&nbsp;&nbsp;&nbsp;&nbsp;`experiment_results.csv` – bảng n_components vs accuracy vs variance*
