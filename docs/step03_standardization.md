# Bước 3: Feature Engineering (Standardization)

> **Trạng thái**: Hoàn thành  

---

## 1. Goal (Mục tiêu)
Chuẩn hóa thang đo của tất cả các đặc trưng về cùng một phân phối (Mean = 0, Std = 1). Đây là bước bắt buộc vì PCA rất nhạy cảm với độ lớn của thang đo (các đặc trưng có biên độ lớn như `Proline` sẽ chiếm ưu thế hoàn toàn so với các đặc trưng nhỏ như `Ash` nếu không chuẩn hóa).

## 2. Input
- Clean Dataset từ Bước 2.

## 3. Tasks & Results (Công việc & Kết quả thực tế)
### Các công việc đã thực hiện:
1. Tách ma trận đặc trưng $X$ (13 cột ban đầu) và nhãn lớp $y$.
2. Khởi tạo thuật toán chuẩn hóa `StandardScaler`.
3. Tính toán trọng số (Mean, Std) và chuyển đổi dữ liệu.

### Kết quả thu được:
- **Thông số dữ liệu sau chuẩn hóa:**
  - Kỳ vọng trung bình (Mean): **-0.0000** (xấp xỉ bằng 0)
  - Độ lệch chuẩn (Std): **1.0000** (bằng đúng 1)
- Dữ liệu của tất cả 13 đặc trưng đã có chung một thang đo, sẵn sàng để tính toán ma trận hiệp phương sai của PCA.

## 4. Output & Visuals (Sản phẩm đầu ra)
- Ma trận đặc trưng đã scale (`X_train_scaled`, `X_test_scaled`).

## 5. Insight (Nhận định)
Việc chuẩn hóa đã xóa bỏ hoàn toàn sự thống trị của đặc trưng `Proline` (có giá trị trung bình ~746.9, lớn gấp hàng trăm lần các đặc trưng khác). Bây giờ, mọi đặc trưng đều có tiếng nói ngang nhau trong việc đóng góp vào phương sai của toàn hệ thống.

## 6. Decision (Quyết định tiếp theo)
Chuyển sang **Bước 4: Data Split** để phân tách dữ liệu huấn luyện và kiểm thử một cách an toàn.

## 7. Artifacts (Danh mục lưu trữ)
- Bộ tham số chuẩn hóa (Scaler weights).
