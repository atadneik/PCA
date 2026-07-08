# Bước 4: Data Split

> **Trạng thái**: Hoàn thành  

---

## 1. Goal (Mục tiêu)
Phân chia tập dữ liệu để fit PCA và huấn luyện/đánh giá downstream model một cách công bằng, đảm bảo chỉ tính toán trọng số (fit Scaler và PCA) trên tập Train để tránh rò rỉ dữ liệu (data leakage) sang tập Test.

## 2. Input
- Scaled Feature Set từ Bước 3.

## 3. Tasks & Results (Công việc & Kết quả thực tế)
### Các công việc đã thực hiện:
1. Chia dữ liệu theo tỷ lệ 80% Train và 20% Test.
2. Thiết lập tham số phân tầng `stratify=y` dựa trên phân phối nhãn lớp.
3. Cài đặt `random_state=42` để đảm bảo kết quả tái lập.

### Kết quả thu được:
- **Kích thước các tập dữ liệu:**
  - Tập huấn luyện (Train set): **142 mẫu, 13 đặc trưng**
  - Tập kiểm thử (Test set): **36 mẫu, 13 đặc trưng**
- **Tỷ lệ phân phối nhãn lớp (Train vs Test):**
  - Train: Class 2 (40.1%), Class 1 (33.1%), Class 3 (26.8%)
  - Test: Class 2 (38.9%), Class 1 (33.3%), Class 3 (27.8%)
  - Đảm bảo tỷ lệ các lớp đồng đều hoàn hảo giữa hai tập.

## 4. Output & Visuals (Sản phẩm đầu ra)
- Phân chia thành công 4 tập: `X_train`, `X_test`, `y_train`, `y_test`.

## 5. Insight (Nhận định)
Việc sử dụng chia dữ liệu phân tầng (`stratify`) giúp loại bỏ nguy cơ lệch nhãn trong tập Test nhỏ (36 mẫu), đảm bảo việc đánh giá mô hình phân loại sau này có độ tin cậy cao nhất.

## 6. Decision (Quyết định tiếp theo)
Huấn luyện mô hình cơ sở ở **Bước 5: Baseline Model Setup** để lấy mốc đối chứng.

## 7. Artifacts (Danh mục lưu trữ)
- Code chia tập dữ liệu trong script chính.
