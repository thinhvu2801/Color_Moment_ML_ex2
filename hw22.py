import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew


# Hàm tính Mean, Std, Skewness của các kênh màu BGR cho một ảnh


def calculate_color_moments(image):
    channels = cv2.split(image)
    moments = []

    for channel in channels:
        mean = np.mean(channel)
        std = np.std(channel)
        skewness = skew(channel.flatten())
        moments.append((mean, std, skewness))

    return moments


# Hàm tính Distance of Moments (DOM) giữa hai vector đặc trưng (Mean, Std, Skewness)


def dom_distance(features1, features2):
    dom = 0
    for i in range(len(features1)):
        for j in range(3):  # 3 moments: Mean, Std, Skewness
            dom += (features1[i][j] - features2[i][j]) ** 2
    return np.sqrt(dom)


# Hiển thị ảnh sử dụng matplotlib
def display_images(image_paths):
    fig, axes = plt.subplots(1, len(image_paths), figsize=(15, 5))
    for i, image_path in enumerate(image_paths):
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Chuyển sang định dạng RGB để hiển thị
        axes[i].imshow(image)
        axes[i].axis('off')
        axes[i].set_title(f"Image {i + 1}")
    plt.show()


# Hiển thị biểu đồ Mean Color Moments


def plot_color_moments(means, image_names):
    labels = ['Mean B', 'Mean G', 'Mean R']
    x = np.arange(len(image_names))  # các vị trí cho các ảnh

    fig, ax = plt.subplots(figsize=(10, 6))

    for i in range(3):  # Ba kênh màu B, G, R
        ax.bar(x + i * 0.2, [mean[i] for mean in means], width=0.2, label=labels[i])

    ax.set_xlabel('Images')
    ax.set_ylabel('Mean Color Moments')
    ax.set_title('Mean Color Moments for Each Image')
    ax.set_xticks(x + 0.2)
    ax.set_xticklabels(image_names)
    ax.legend()
    plt.show()


# Đường dẫn đến các hình ảnh (thay đường dẫn)
image_paths = ['C://DISK D/CCTCC/MachineLearning/white.jpg', 'C://DISK D/CCTCC/MachineLearning/pink.jpg', 'C://DISK D/CCTCC/MachineLearning/red.jpg']  # Thay đường dẫn tới hình ảnh

# Tính toán giá trị Color Moments cho từng ảnh
color_moments = []
image_names = []
for image_path in image_paths:
    image = cv2.imread(image_path)
    moments = calculate_color_moments(image)
    color_moments.append(moments)  # Lưu cả Mean, Std, Skewness cho mỗi kênh màu
    image_names.append(image_path.split('/')[-1])  # Lưu tên ảnh
    print(f"Color Moments for {image_path}: {moments}")

# Tính khoảng cách DOM giữa từng cặp ảnh
distances = {}
for i in range(len(color_moments)):
    for j in range(i + 1, len(color_moments)):
        distance = dom_distance(color_moments[i], color_moments[j])
        distances[f'Image {i + 1} vs Image {j + 1}'] = distance

# In ra khoảng cách DOM giữa các cặp ảnh
print("\nKhoảng cách DOM giữa các ảnh:")
for pair, distance in distances.items():
    print(f"{pair}: {distance:.2f}")

# Hiển thị các ảnh
display_images(image_paths)

# Hiển thị biểu đồ cho Mean Color Moments
means_only = [moments[0] for moments in color_moments]  # Lấy giá trị Mean từ Color Moments
plot_color_moments(means_only, image_names)

# Tìm ảnh có màu sắc tương đồng nhất (khoảng cách DOM nhỏ nhất)
most_similar_pair = min(distances, key=distances.get)
print(f"\nẢnh có màu sắc tương đồng nhất: {most_similar_pair} với khoảng cách: {distances[most_similar_pair]:.2f}")
