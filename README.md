# **Color Moments - Machine Learning Demo**

Đây là một ví dụ demo về việc tính toán **Color Moments** (Mean, Std, Skewness) cho các kênh màu **BGR** của một tập ảnh, từ đó tính toán mức độ tương đồng giữa các ảnh dựa trên các đặc trưng này. Đây là một bài tập cơ bản trong lĩnh vực học máy liên quan đến xử lý và phân tích ảnh.

### **Color Moments**
Color Moments là các đặc trưng thống kê dùng để mô tả màu sắc của một ảnh. Chúng bao gồm:
1. **Mean (Trung bình)**: Giá trị trung bình của cường độ màu.
2. **Std (Độ lệch chuẩn)**: Độ biến thiên của cường độ màu.
3. **Skewness (Độ lệch)**: Độ bất đối xứng của phân bố cường độ màu.

Việc tính toán ba giá trị này cho mỗi kênh màu (B, G, R) giúp phân tích và so sánh màu sắc giữa các ảnh.

## **Yêu cầu cài đặt**
### **Thư viện cần thiết**
- `OpenCV`: Thư viện xử lý ảnh.
- `NumPy`: Thư viện tính toán mảng.
- `Matplotlib`: Thư viện vẽ biểu đồ.
- `SciPy`: Thư viện hỗ trợ tính toán các đặc trưng thống kê.

Cài đặt các thư viện cần thiết bằng lệnh:
```bash
pip install opencv-python numpy matplotlib scipy
