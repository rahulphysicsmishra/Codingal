# Colab-friendly: use cv2_imshow (works in headless Colab)
from google.colab.patches import cv2_imshow
import cv2
import os
import matplotlib.pyplot as plt

# Make sure file exists in current working directory
file_name = '/content/arr_.jpg'
if not os.path.isfile(file_name):
    print(f"File not found: {file_name}. Upload it via the Files pane or use files.upload().")
else:
    image = cv2.imread(file_name)
    if image is None:
        print("cv2.imread returned None — the file may be corrupted or unsupported.")
    else:
        # OpenCV uses BGR order; converting to RGB for matplotlib for nicer colors
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Display with cv2_imshow (works in Colab)
        print("Displaying with cv2_imshow:")
        cv2_imshow(image)  # cv2_imshow expects BGR image; it converts internally for Colab

        # Also show using matplotlib (optional)
        print("Displaying with matplotlib (RGB):")
        plt.figure(figsize=(8, 5))
        plt.imshow(image_rgb)
        plt.axis('off')
        plt.show()

        # Print safe image info
        print("Image Dimensions (H, W, C):", image.shape)