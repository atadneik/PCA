# Bước 5: Baseline Model Setup

> **Trạng thái**: Hoàn thành  

---

## 1. Goal (Mục tiêu)
Xây dựng mốc so sánh (benchmark) tối thiểu sử dụng toàn bộ 13 đặc trưng gốc để làm tiêu chuẩn đối chứng cho các thử nghiệm giảm chiều bằng PCA phía sau.

## 2. Input
- Tập dữ liệu Train/Test gốc đã scale: `X_train_scaled`, `X_test_scaled` và nhãn `y_train`, `y_test`.

## 3. Tasks & Results (Công việc & Kết quả thực tế)
### Các công việc đã thực hiện:
1. Khởi tạo mô hình phân loại Logistic Regression với số lần lặp tối đa `max_iter=1000`.
2. Huấn luyện (fit) mô hình trên 13 đặc trưng gốc của tập Train.
3. Dự đoán và đánh giá hiệu năng trên tập Test.

### Kết quả thu được:
- **Độ chính xác Baseline (Test Accuracy):** **97.22%** (Dự đoán đúng 35/36 mẫu).
- **Chi tiết phân loại (Classification Report):**
  - **Class 1:** Precision: 1.00, Recall: 1.00, F1-score: 1.00 (12 mẫu)
  - **Class 2:** Precision: 0.93, Recall: 1.00, F1-score: 0.97 (14 mẫu)
  - **Class 3:** Precision: 1.00, Recall: 0.90, F1-score: 0.95 (10 mẫu)

## 4. Output & Visuals (Sản phẩm đầu ra)
- Mô hình Baseline đã được huấn luyện.
- Báo cáo hiệu năng phân loại cơ sở.

## 5. Insight (Nhận định)
Hiệu năng phân loại trên toàn bộ 13 đặc trưng gốc đạt mức cực kỳ xuất sắc (97.22%). Điều này chứng tỏ dữ liệu gốc có khả năng phân tách tuyến tính rất mạnh. Mô hình PCA sau khi giảm số chiều cần đạt hiệu năng xấp xỉ mức này để chứng minh việc giảm chiều không làm suy giảm chất lượng phân loại.

## 6. Decision (Quyết định tiếp theo)
Chuyển sang **Bước 6: PCA Fit & Component Selection** để bắt đầu giảm chiều dữ liệu.

## 7. Artifacts (Danh mục lưu trữ)
- Metrics báo cáo Baseline Accuracy.
