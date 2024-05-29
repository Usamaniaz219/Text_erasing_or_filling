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



# import cv2
# import numpy as np

# # Read the mask image
# # mask_image = cv2.imread("/home/usama/Median_erode__contours_low__and_high_resolution_test/LUV_Meanshift_Bandwidth_8_fahad_results/ca_gilroy/ca_gilroy_7.jpg", cv2.IMREAD_GRAYSCALE)
# mask_image = cv2.imread("/home/usama/Median_erode__contours_low__and_high_resolution_test/LUV_Meanshift_Bandwidth_8_fahad_results/ca_emeryville/ca_emeryville_15.jpg", cv2.IMREAD_GRAYSCALE)
# # Find contours in the mask image
# contours, _ = cv2.findContours(mask_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Create a blank mask to draw the filtered contours
# filtered_mask = np.zeros_like(mask_image)

# # Iterate through the contours
# for contour in contours:
#     # Convert contour to polygon
#     epsilon = 0.01 * cv2.arcLength(contour, True)
#     approx_polygon = cv2.approxPolyDP(contour, epsilon, True)
    
#     # Check if the polygon has more than 16 vertices
#     if len(approx_polygon) > 3:
#         # Calculate the bounding rectangle of the contour
#         x, y, w, h = cv2.boundingRect(contour)
        
#         # Check if the interior width is less than 2 pixels
#         if w > 20:
#             # Draw the contour on the filtered mask
#             cv2.drawContours(filtered_mask, [contour], -1, 255, thickness=cv2.FILLED)

# # Display the filtered mask
# cv2.imshow("Filtered Mask", cv2.resize(filtered_mask, (900, 900)))
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# import numpy as np
# from shapely.geometry import Polygon, Point

# # Load the binary mask image
# mask = cv2.imread('/home/usama/Testing_/ca_gilroy_7_filled_contours.png', cv2.IMREAD_GRAYSCALE)
# _, mask = cv2.threshold(mask, 25, 255, cv2.THRESH_BINARY)
# mask = cv2.medianBlur(mask, 3)

# # Find contours in the binary mask image
# contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Create a blank image to draw the filtered contours
# filtered_image = np.zeros_like(mask)

# # Iterate through each contour
# for cnt in contours:
#     if len(cnt) >= 4:  # Filter out contours with less than 4 points
#         # Convert contour to a Shapely Polygon
#         points = [Point(coord[0][0], coord[0][1]) for coord in cnt]
#         polygon = Polygon([[p.x, p.y] for p in points])

#         # Calculate the compactness of the polygon
#         compactness = polygon.area / (polygon.length ** 2)

#         # Filter out contours with high compactness (near to lines)
#         if compactness <0.2:  # Adjust the threshold as needed
#             cv2.drawContours(filtered_image, [cnt], 0, 255, -1)

# # Convert the filtered image to 8-bit unsigned integer format
# filtered_image = np.uint8(filtered_image)

# # Save the filtered image
# cv2.imwrite("/home/usama/Median_erode__contours_low__and_high_resolution_test/neighbourhood_based_contour_filtering_based_representative_point/result_ca_gilroy_7_after.jpg", filtered_image)

# # Display the filtered image
# cv2.imshow('Filtered Image', filtered_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



