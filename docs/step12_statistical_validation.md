# Bước 12: Statistical Validation

> **Trạng thái**: Hoàn thành  

---

## 1. Goal (Mục tiêu)
Kiểm chứng độ tin cậy bằng toán học thống kê để xem sự chênh lệch hiệu năng giữa Baseline CV và PCA CV (2 components) là thực sự khác biệt hay chỉ là do ngẫu nhiên.

## 2. Input
- Các điểm số CV scores của Baseline và PCA 2-components thu được từ Bước 10.

## 3. Tasks & Results (Công việc & Kết quả thực tế)
### Các công việc đã thực hiện:
1. Thực hiện phép kiểm định thống kê Paired t-test (kiểm định t phụ thuộc) trên điểm số CV.
2. Tính toán khoảng tin cậy 95% (95% Confidence Interval - CI) cho độ chính xác của hai mô hình.

### Kết quả thu được:
- **Chỉ số kiểm định T-test:**
  - Trị số thống kê $t$ (t-statistic): **1.6326**
  - Trị số $p$ (p-value): **0.1779**
- **Kết luận kiểm định:** Vì $p = 0.18 \geq 0.05$, không bác bỏ giả thuyết không ($H_0$). Sự giảm nhẹ $1.41\%$ độ chính xác khi dùng PCA 2 chiều **không có ý nghĩa thống kê**.
- **Khoảng tin cậy 95% (95% CI):**
  - Khoảng tin cậy của PCA CV Accuracy: **[91.26%, 101.75%]**
  - Khoảng tin cậy của Baseline CV Accuracy: **[94.06%, 101.75%]**
  - Hai khoảng tin cậy chồng lấp lên nhau rất nhiều, chứng tỏ hiệu năng hai mô hình tương đương nhau.

## 4. Output & Visuals (Sản phẩm đầu ra)
- Báo cáo kết quả kiểm định giả thuyết thống kê.

## 5. Insight (Nhận định)
Mặc dù dùng 2 chiều làm giảm nhẹ độ chính xác kiểm thử, phép kiểm định T-test khẳng định sự suy giảm này hoàn toàn có thể là do phân bố ngẫu nhiên của các Fold dữ liệu chứ không phải do mô hình PCA yếu hơn. Do đó, việc chấp nhận giảm 85% chiều dữ liệu để đổi lấy sự đơn giản là quyết định hoàn toàn hợp lý về mặt khoa học dữ liệu.

## 6. Decision (Quyết định tiếp theo)
Chuyển sang **Bước 13: Error & Reconstruction Analysis** để phân tích các mẫu dự đoán lỗi của mô hình PCA.

## 7. Artifacts (Danh mục lưu trữ)
- Thống kê t-statistic, p-value và Confidence Intervals trong báo cáo.
