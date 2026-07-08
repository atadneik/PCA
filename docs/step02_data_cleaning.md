# Bước 2: Data Cleaning

> **Trạng thái**: Hoàn thành  

---

## 1. Goal (Mục tiêu)
Làm sạch dữ liệu bằng cách xử lý các giá trị khuyết thiếu (missing values), hàng trùng lặp (duplicates) và kiểm soát các ngoại lệ (outliers) để tránh làm lệch hướng các trục chính của PCA.

## 2. Input
- Raw Dataset + Nhận định phân phối từ Bước 1.

## 3. Tasks & Results (Công việc & Kết quả thực tế)
### Các công việc đã thực hiện:
1. Kiểm tra sự tồn tại của các giá trị khuyết thiếu (Null/NaN) trên tất cả các cột.
2. Kiểm tra các hàng dữ liệu bị lặp hoàn toàn (duplicated rows).
3. Loại bỏ trùng lặp nếu có và xác nhận kích thước dữ liệu sạch.

### Kết quả thu được:
- **Số lượng giá trị khuyết thiếu (Missing values):** 0 (Không có giá trị thiếu ở bất kỳ cột nào).
- **Số hàng trùng lặp (Duplicated rows):** 0.
- **Kích thước dữ liệu sạch:** 178 mẫu, 14 cột (giữ nguyên kích thước gốc).

## 4. Output & Visuals (Sản phẩm đầu ra)
- Bộ dữ liệu sạch đã được xác thực (Cleaned Dataset).

## 5. Insight (Nhận định)
UCI Wine Recognition là một bộ dữ liệu có chất lượng thu thập rất tốt, không chứa các dòng lỗi cấu trúc hay mất mát thông tin. Các giá trị ngoại lệ (outliers) phát hiện ở Bước 1 phản ánh biến động tự nhiên của các thành phần hóa học trong rượu chứ không phải do lỗi nhập liệu, vì vậy quyết định giữ nguyên các điểm này để không làm mất tính tổng quát của phân tích.

## 6. Decision (Quyết định tiếp theo)
Chuyển sang **Bước 3: Feature Engineering** để thực hiện chuẩn hóa dữ liệu.

## 7. Artifacts (Danh mục lưu trữ)
- Cleaned Dataset.
