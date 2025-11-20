import cv2
from google.colab.patches import cv2_imshow
import os

file_path = '/content/arr_.jpg'

# Check if file exists
if not os.path.isfile(file_path):
    raise FileNotFoundError(f"File not found: {file_path}")

# Load the image
image = cv2.imread(file_path)

if image is None:
    raise ValueError("cv2.imread() failed — image may be corrupted or unsupported.")

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize to 224x224
resized_image = cv2.resize(gray_image, (224, 224))

# Display image inside Colab
print("Displaying processed image:")
cv2_imshow(resized_image)

# Save the processed image automatically (since we cannot wait for keypress)
save_path = '/content/grayscale_resized_image.jpg'
cv2.imwrite(save_path, resized_image)

print(f"Image saved as: {save_path}")

# Print processed image properties
print("Processed Image Dimensions:", resized_image.shape)
