# ML Pipeline Rules — PCA Dimensionality Reduction Project

## Nguyên tắc cốt lõi

> **Controlled Experiment**: Chỉ thay đổi **1 biến** ở mỗi lần thử nghiệm (ví dụ: thay đổi số lượng components, giữ nguyên phương pháp scaling).
> Không bao giờ bỏ qua bước. Không bao giờ chuyển bước khi artifact chưa hoàn thành.

---

## Quy trình bắt buộc — 14 Bước Pipeline cho PCA

Agent **PHẢI** tuân thủ đúng thứ tự 14 bước dưới đây. Mỗi bước phải hoàn tất trước khi chuyển sang bước tiếp theo.

### Cấu trúc mỗi Bước

Mỗi bước khi thực hiện **BẮT BUỘC** phải tuân thủ nghiêm ngặt 7 thành phần (Vibe Coding Checklist):

1. **Goal** — Mục tiêu cụ thể của bước
2. **Input** — Dữ liệu/artifact đầu vào (từ bước trước)
3. **Tasks** — Danh sách công việc cần thực hiện chi tiết
4. **Output** — Sản phẩm đầu ra cụ thể
5. **Insight** — Nhận định rút ra được sau khi phân tích
6. **Decision** — Quyết định hành động tiếp theo (tiếp tục / quay lại / điều chỉnh)
7. **Artifact** — File code, biểu đồ, file kết quả, hoặc báo cáo lưu trữ

---

### Bước 1 — EDA
- **Goal**: Phân tích đặc điểm phân phối và mối tương quan giữa các đặc trưng gốc để đánh giá mức độ dư thừa thông tin.
- **Input**: Raw dataset (`Wine dataset.csv`).
- **Tasks**: Phân tích phân phối (Distribution), phát hiện giá trị thiếu (Missing values), nhận diện ngoại lệ (Outliers - cực kỳ quan trọng vì PCA rất nhạy cảm với outlier), phân tích ma trận tương quan (Correlation Matrix) để tìm các nhóm biến đồng biến/nghịch biến.
- **Output**: Data Profile & Correlation Report.
- **Insight**: Các biến có tương quan mạnh với nhau không? (Nếu tương quan mạnh, PCA sẽ hoạt động rất hiệu quả).
- **Decision**: Xác định các biến cần xử lý nhiễu ở Bước 2.
- **Artifact**: Cập nhật file code phân tích, lưu biểu đồ tương quan vào thư mục `Figures/`.

### Bước 2 — Data Cleaning
- **Goal**: Xử lý dữ liệu khuyết thiếu, trùng lặp và loại bỏ/cắt (capping) các ngoại lệ (outliers) để tránh làm lệch các trục chính của PCA.
- **Input**: Raw dataset + Insight từ Bước 1.
- **Tasks**: Điền/xóa Missing values, xử lý Duplicate, xử lý Outliers (ví dụ: dùng phương pháp IQR hoặc Z-score).
- **Output**: Clean Dataset.
- **Insight**: Dữ liệu đã đủ sạch và các trị số ngoại lệ đã được kiểm soát chưa?
- **Decision**: Chuyển sang Feature Engineering nếu dữ liệu đạt chuẩn.
- **Artifact**: Dữ liệu sạch đã lưu.

### Bước 3 — Feature Engineering (Standardization)
- **Goal**: Chuẩn hóa thang đo của các đặc trưng để tránh các biến có phương sai lớn thống trị các thành phần chính.
- **Input**: Clean Dataset.
- **Tasks**: Thực hiện Scaling (thường dùng StandardScaler vì PCA yêu cầu dữ liệu có Mean=0 và Var=1).
- **Output**: Scaled Feature Set (Ma trận X chuẩn hóa, vector y nếu có).
- **Insight**: Xác nhận giá trị Mean xấp xỉ 0 và Std xấp xỉ 1 trên toàn bộ các cột.
- **Decision**: Chốt ma trận dữ liệu chuẩn hóa để chuẩn bị phân tách.
- **Artifact**: Hàm chuẩn hóa dữ liệu, tài liệu chứng minh dữ liệu đã scale thành công.

### Bước 4 — Data Split
- **Goal**: Phân chia tập dữ liệu để fit PCA và huấn luyện/đánh giá downstream model một cách công bằng, tránh rò rỉ dữ liệu (data leakage).
- **Input**: Scaled Feature Set.
- **Tasks**: Chia tập Train/Test (hoặc Train/Val/Test). Đảm bảo chỉ fit Scaler và PCA trên tập Train, sau đó áp dụng phép biến đổi (transform) lên tập Test.
- **Output**: Dataset Split (Train/Val/Test).
- **Insight**: Tỷ lệ phân phối các lớp (nếu là classification downstream) có cân bằng giữa các tập không?
- **Decision**: Xác nhận các tập dữ liệu để bắt đầu modeling.
- **Artifact**: Code chia dữ liệu an toàn trong file script.

### Bước 5 — Baseline Model Setup
- **Goal**: Xây dựng mốc so sánh (benchmark) tối thiểu sử dụng toàn bộ các đặc trưng gốc (chưa giảm chiều).
- **Input**: Dataset Split (Train/Test gốc).
- **Tasks**: Huấn luyện một downstream model (ví dụ: Logistic Regression hoặc Linear Regression) trên 100% các đặc trưng gốc sau khi scale.
- **Output**: Baseline Metrics (Accuracy, F1-score hoặc RMSE).
- **Insight**: Hiệu năng tối đa đạt được khi sử dụng toàn bộ thông tin gốc là bao nhiêu?
- **Decision**: Lấy kết quả này làm tiêu chuẩn đối chứng. Mọi mô hình giảm chiều sau đó phải so sánh với mốc này.
- **Artifact**: Ghi nhận kết quả baseline vào báo cáo.

### Bước 6 — PCA Fit & Component Selection
- **Goal**: Huấn luyện mô hình PCA trên tập Train và lựa chọn số lượng thành phần chính ban đầu (ví dụ: n_components=2 để trực quan hóa).
- **Input**: Train set đã chuẩn hóa.
- **Tasks**: Khởi tạo PCA, fit trên tập Train và biến đổi (transform) cả Train và Test sang không gian mới. Vẽ Scree Plot và đồ thị phương sai tích lũy (Cumulative Explained Variance).
- **Output**: Trực quan hóa dữ liệu trên không gian PCA mới (2D/3D Scatter Plot) và danh sách cấu phần ban đầu.
- **Insight**: Trực quan hóa 2D cho thấy các lớp dữ liệu có phân tách rõ ràng không? Elbow point xuất hiện tại thành phần thứ mấy?
- **Decision**: Chọn số lượng thành phần chính (n) phù hợp cho việc phân tích và downstream task.
- **Artifact**: Đồ thị Scree Plot, đồ thị Cumulative Variance và Scatter plot 2D.

### Bước 7 — Hyperparameter Tuning (n_components Selection)
- **Goal**: Tìm số lượng thành phần chính tối ưu để giữ lại lượng thông tin mong muốn (ví dụ: chọn n để đạt threshold phương sai tích lũy ≥ 95%).
- **Input**: Scree Plot & Cumulative Variance.
- **Tasks**: Tìm điểm thỏa mãn điều kiện giữ lại lượng phương sai mục tiêu (ví dụ: 90%, 95%) hoặc thực hiện quét (sweep) số lượng components để xem ảnh hưởng đến hiệu năng downstream model.
- **Output**: Optimal number of components.
- **Insight**: Cần tối thiểu bao nhiêu components để giữ được phần lớn thông tin cốt lõi mà không bị mất mát quá nhiều?
- **Decision**: Chốt số lượng thành phần chính cuối cùng cho mô hình PCA chính thức.
- **Artifact**: File lưu tham số tối ưu (best n_components).

### Bước 8 — Final PCA Transformation
- **Goal**: Thực hiện giảm chiều dữ liệu bằng mô hình PCA tối ưu cuối cùng.
- **Input**: Dataset Split, Optimal n_components.
- **Tasks**: Fit PCA với số lượng components tối ưu trên tập Train, transform tập Train và Test sang ma trận thành phần chính mới.
- **Output**: Reduced Feature Sets (X_train_pca, X_test_pca).
- **Insight**: Xác nhận chiều dữ liệu đã được giảm thành công theo đúng cấu hình.
- **Decision**: Sẵn sàng đưa dữ liệu đã giảm chiều sang bước đánh giá hiệu năng downstream.
- **Artifact**: Ma trận dữ liệu giảm chiều.

### Bước 9 — PCA Evaluation Metrics
- **Goal**: Đánh giá chất lượng của phép giảm chiều PCA thông qua các chỉ số định lượng.
- **Input**: Reduced Feature Sets, PCA model.
- **Tasks**: Tính toán tỷ lệ phương sai giải thích được (Explained Variance Ratio), Tỷ lệ giảm chiều (Dimensionality Reduction Ratio), và Sai số tái dựng (Reconstruction Error/MSE) từ không gian giảm chiều ngược lại không gian gốc.
- **Output**: PCA Metrics Report.
- **Insight**: Lượng thông tin bị mất mát (Information Loss) là bao nhiêu? Sai số tái dựng giữa Train và Test có ổn định không?
- **Decision**: Chất lượng giảm chiều có chấp nhận được không trước khi mang đi huấn luyện downstream model.
- **Artifact**: Bảng chỉ số đánh giá PCA và sai số tái dựng.

### Bước 10 — Cross Validation
- **Goal**: Đánh giá độ ổn định của dữ liệu sau khi giảm chiều bằng phương pháp kiểm chứng chéo trên downstream model.
- **Input**: Reduced Feature Sets.
- **Tasks**: Thực hiện K-Fold Cross Validation trên tập Train đã giảm chiều sử dụng downstream model. So sánh trực tiếp với CV score của Baseline.
- **Output**: CV Mean ± Std của downstream metrics.
- **Insight**: Việc giảm chiều có làm tăng độ lệch chuẩn (Std) hoặc làm giảm độ ổn định của mô hình khi tập huấn luyện thay đổi không?
- **Decision**: Xác nhận độ ổn định của các đặc trưng PCA mới.
- **Artifact**: Kết quả log cross-validation và biểu đồ so sánh phân phối CV (Boxplot).

### Bước 11 — Experiment Management
- **Goal**: Theo dõi, so sánh và quản lý kết quả của các thử nghiệm giảm chiều với các cấu hình n_components khác nhau.
- **Input**: Kết quả quét (sweep) từ n_components = 1 đến tối đa.
- **Tasks**: Log lại: n_components, Explained Variance, Downstream Accuracy/Loss, Reconstruction Error tương ứng. Vẽ đồ thị trục kép (Dual-axis chart) so sánh các tham số này.
- **Output**: Experiment History log.
- **Insight**: Đâu là "sweet spot" (điểm tối ưu) - nơi số chiều giảm tối đa nhưng hiệu năng downstream model vẫn được giữ nguyên hoặc cải thiện?
- **Decision**: Chọn cấu hình tốt nhất làm kết quả chính thức cho dự án.
- **Artifact**: File kết quả `experiment_results.csv` và đồ thị sweep.

### Bước 12 — Statistical Validation
- **Goal**: Kiểm chứng mức độ tin cậy bằng thống kê đối với sự chênh lệch hiệu năng giữa mô hình Baseline và PCA model.
- **Input**: CV scores của Baseline và PCA downstream model.
- **Tasks**: Thực hiện kiểm định thống kê (ví dụ: Paired t-test) trên các điểm số kiểm chứng chéo để xem sự thay đổi hiệu năng có ý nghĩa thống kê không.
- **Output**: Statistical Hypothesis Testing Report (p-value, Confidence Intervals).
- **Insight**: Việc giảm chiều có thực sự làm giảm đáng kể hiệu năng của mô hình không? Hay sự sụt giảm/tăng nhẹ chỉ là do ngẫu nhiên (p-value ≥ 0.05)?
- **Decision**: Chấp nhận sử dụng số chiều đã giảm nếu không có sự sụt giảm hiệu năng có ý nghĩa thống kê.
- **Artifact**: Chỉ số t-statistic, p-value và Confidence Intervals (Khoảng tin cậy).

### Bước 13 — Error & Reconstruction Analysis
- **Goal**: Phân tích các trường hợp dữ liệu bị mô hình dự đoán sai sau khi giảm chiều, hoặc các vùng dữ liệu có sai số tái dựng lớn nhất.
- **Input**: Predictions, Ground Truth trên Test set, Reconstruction Residuals.
- **Tasks**: Phân tích ma trận nhầm lẫn (Confusion Matrix) của downstream model, tìm các điểm dữ liệu bị misclassified và đối chiếu tọa độ của chúng trên không gian PCA 2D để xem chúng có nằm ở vùng ranh giới (chồng lấp) không.
- **Output**: Error & Reconstruction Analysis Report.
- **Insight**: Các mẫu bị lỗi có đặc điểm chung gì? Lỗi phát sinh do giảm chiều làm mất ranh giới phân tách hay do dữ liệu gốc bị nhiễu?
- **Decision**: Đưa ra hướng xử lý (ví dụ: tăng components hoặc quay lại bước Cleaning dữ liệu).
- **Artifact**: Biểu đồ Confusion Matrix và danh sách các điểm dữ liệu lỗi.

### Bước 14 — Model Interpretability (Feature Loadings)
- **Goal**: Giải thích ý nghĩa vật lý/kinh doanh của các thành phần chính (PCs) dựa trên các đặc trưng gốc.
- **Input**: PCA components (Feature Loadings).
- **Tasks**: Trích xuất trọng số (loadings) của các đặc trưng gốc đóng góp vào PC1, PC2... Vẽ biểu đồ Loading Bar Chart hoặc Biplot (kết hợp Scatter plot dữ liệu và vector hướng đóng góp của đặc trưng gốc).
- **Output**: Interpretability & Loadings Report.
- **Insight**: PC1 và PC2 đại diện cho những thuộc tính/khái niệm thực tế nào? Biến gốc nào đóng vai trò quan trọng nhất trong việc định hình các PC?
- **Decision**: Chốt báo cáo giải thích mô hình để đưa vào vận hành thực tế.
- **Artifact**: Biểu đồ Feature Loadings, đồ thị Biplot và tổng kết dự án.

---

## Quy tắc thực hiện

### Controlled Experiment
- **BẮT BUỘC**: Chỉ thay đổi 1 biến mỗi lần thử nghiệm (ví dụ: khi so sánh các n_components khác nhau, giữ nguyên phương pháp Scaler và tham số của downstream model).
- Log đầy đủ: dataset version, n_components, metrics (accuracy, reconstruction error, explained variance).

### Gate Checking (Điều kiện chuyển bước)
- Không chuyển sang bước tiếp theo nếu các phép tính hoặc biểu đồ tương ứng chưa được thực hiện xong.
- Mỗi bước phải có nhận định (Insight) và quyết định hành động tiếp theo (Decision).
- Nếu downstream model hoạt động quá tệ ở các bước đánh giá cuối, phải quay lại các bước trước (Feature Engineering hoặc Tuning n_components) để hiệu chỉnh.

