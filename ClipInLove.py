import cv2
import matplotlib.pyplot as plt

# Prompt the user to enter the path of the image file
file_path = "demo.jpg"

# Read the image
img = cv2.imread(file_path)

if img is not None:
    # Convert the image to RGB for correct color display with Matplotlib
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Display the image using Matplotlib
    plt.imshow(img_rgb)
    plt.axis('off')  # Hide axes
    plt.show()
else:
    print("Image not found. Please check the file path.")
