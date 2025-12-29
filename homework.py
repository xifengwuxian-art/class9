import cv2
import os

image_path = "C:/Users/xifen/Desktop/python/class9/example.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error: image not found, check the path!")
    exit()

height, width = image.shape[:2]

y = height // 3

left_start  = (20, y)           
left_end    = (width - 20, y)

right_start = (width - 20, y)   
right_end   = (20, y)

cv2.arrowedLine(image, left_start, left_end,  (0, 0, 255), 3, tipLength=0.03)
cv2.arrowedLine(image, right_start, right_end, (0, 0, 255), 3, tipLength=0.03)

text = f"Width: {width}px"

text_x = width // 2 - 100   
text_y = y - 20

cv2.putText(
    image,
    text,
    (text_x, text_y),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 255, 0),   
    2,
    cv2.LINE_AA
)

os.makedirs("../output_images", exist_ok=True)
output_path = "../output_images/example_with_width.png"
cv2.imwrite(output_path, image)

print("Done! Saved to:", output_path)

cv2.imshow("Width annotation", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
