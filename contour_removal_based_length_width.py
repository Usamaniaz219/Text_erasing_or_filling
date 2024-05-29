import cv2
import numpy as np

# Read the mask image
mask_image = cv2.imread("/home/usama/Median_erode__contours_low__and_high_resolution_test/LUV_Meanshift_Bandwidth_8_fahad_results/ca_gilroy/ca_gilroy_7.jpg", cv2.IMREAD_GRAYSCALE)
_,mask_image = cv2.threshold(mask_image,20,255,cv2.THRESH_BINARY)

# Find contours in the mask image
contours, _ = cv2.findContours(mask_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a blank mask to draw the filtered contours
filtered_mask = np.zeros_like(mask_image)

# Iterate through the contours
for contour in contours:
    # Calculate the bounding rectangle of the contour
    x, y, w, h = cv2.boundingRect(contour)
    print("height and width",h,w)
    # Filter out contours with almost one-pixel width
    if h<2 and w>15 :  
        # Draw the contour on the filtered mask
        cv2.drawContours(filtered_mask, [contour], -1, 255, thickness=cv2.FILLED)

# Display the filtered mask
cv2.imshow("Filtered Mask", cv2.resize(filtered_mask, (900, 900)))
cv2.waitKey(0)
cv2.destroyAllWindows()




