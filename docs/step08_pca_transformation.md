# Bước 8: Final PCA Transformation

> **Trạng thái**: Hoàn thành  

---

## 1. Goal (Mục tiêu)
Thực hiện giảm chiều dữ liệu bằng mô hình PCA tối ưu cuối cùng (chọn cấu hình $n\_components = 2$ để kiểm tra hiệu năng nén thông tin cực đại) phục vụ downstream classifier.

## 2. Input
- Dữ liệu chuẩn hóa Train/Test và tham số components tối ưu.

## 3. Tasks & Results (Công việc & Kết quả thực tế)
### Các công việc đã thực hiện:
1. Fit mô hình PCA với 2 components trên tập Train.
2. Thực hiện biến đổi (transform) cả tập Train và tập Test sang hệ tọa độ PC mới.
3. Xuất kết quả ma trận giảm chiều ra cấu trúc DataFrame hoàn chỉnh để lưu trữ.

### Kết quả thu được:
- **Kích thước không gian đặc trưng mới:**
  - `X_train_pca` có hình dạng: **(142, 2)**
  - `X_test_pca` có hình dạng: **(36, 2)**
- Dữ liệu giảm chiều được lưu trữ kèm nhãn lớp (`class`) và định danh tập (`set`) gồm các cột: `PC1`, `PC2`, `class`, `set`.

## 4. Output & Visuals (Sản phẩm đầu ra)
- Cấu trúc DataFrame kết quả giảm chiều (`pca_result_df`).
- File kết quả trung gian lưu trữ dữ liệu đã nén.

## 5. Insight (Nhận định)
Chiều dữ liệu đã giảm thành công từ 13 cột xuống còn đúng 2 cột PC1 và PC2. Sự thu gọn dữ liệu này giúp loại bỏ hoàn toàn tính đa cộng tuyến (multicollinearity) vì các cột PC1 và PC2 độc lập tuyến tính tuyệt đối với nhau.

## 6. Decision (Quyết định tiếp theo)
Chuyển sang **Bước 9: PCA Evaluation Metrics** để tính toán các chỉ số nén và sai số tái dựng.

## 7. Artifacts (Danh mục lưu trữ)
- Ma trận dữ liệu nén 2D.
