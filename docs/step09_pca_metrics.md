# Bước 9: PCA Evaluation Metrics

> **Trạng thái**: Hoàn thành  

---

## 1. Goal (Mục tiêu)
Đánh giá chất lượng của phép giảm chiều PCA thông qua các chỉ số định lượng nội tại như tỷ lệ giảm chiều, tỷ lệ thông tin mất mát và sai số tái dựng dữ liệu (Reconstruction Error).

## 2. Input
- Mô hình PCA đã huấn luyện, ma trận nén `X_train_pca`, `X_test_pca`.

## 3. Tasks & Results (Công việc & Kết quả thực tế)
### Các công việc đã thực hiện:
1. Tính toán Tỷ lệ giảm chiều (Dimensionality Reduction Ratio).
2. Tính toán lượng phương sai giải thích được và lượng thông tin bị mất (Information Loss).
3. Thực hiện tái dựng dữ liệu từ không gian 2D ngược về 13D gốc (`inverse_transform`) và tính sai số MSE.

### Kết quả thu được:
- **Tỷ lệ giảm số chiều:** **84.62%** (Giảm từ 13 đặc trưng xuống còn 2 thành phần chính).
- **Tổng lượng thông tin giữ lại (Explained Variance):** **55.06%**.
- **Lượng thông tin bị mất mát:** **44.94%**.
- **Sai số tái dựng dữ liệu (Reconstruction MSE):**
  - Trên tập huấn luyện (Train MSE): **0.4494**
  - Trên tập kiểm thử (Test MSE): **0.4732**

## 4. Output & Visuals (Sản phẩm đầu ra)
- Bảng chỉ số đánh giá PCA và sai số tái dựng.

## 5. Insight (Nhận định)
Việc chỉ sử dụng 2 components giúp nén dữ liệu rất mạnh (giảm gần 85% bộ nhớ) nhưng phải đánh đổi bằng việc mất đi 45% thông tin gốc. Tuy nhiên, sai số tái dựng trên tập Test (0.4732) gần như tương đương tập Train (0.4494), cho thấy mô hình PCA học được cấu trúc chung rất vững vàng, không bị overfitting.

## 6. Decision (Quyết định tiếp theo)
Chuyển sang **Bước 10: Cross Validation** để kiểm chứng chéo độ ổn định trên mô hình phân loại.

## 7. Artifacts (Danh mục lưu trữ)
- Báo cáo chất lượng giảm chiều PCA.
