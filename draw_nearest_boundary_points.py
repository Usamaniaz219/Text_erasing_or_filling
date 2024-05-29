


import cv2
import numpy as np
from shapely.geometry import Polygon, Point

import cv2
import numpy as np

# Load the mask image
mask = cv2.imread('/home/usama/Median_erode__contours_low__and_high_resolution_test/centre_based_removing_Contour_logic_results/Failure_Cases_Centre_based_logic/demo117_4.jpg', cv2.IMREAD_GRAYSCALE)

# Find contours in the mask image
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Convert contours to Shapely Polygon objects and calculate representative point
for cnt in contours:
    if len(cnt) >=4:
        # Convert contour to a Shapely Polygon
        points = [Point(coord[0][0], coord[0][1]) for coord in cnt]
        polygon = Polygon([[p.x, p.y] for p in points])
        
        # Calculate representative point
        rep_point = polygon.representative_point()
        rep_x, rep_y = int(rep_point.x), int(rep_point.y)
        for i in range(mask.shape[0]):
            for j in range(mask.shape[1]):
                dist = np.sqrt((i-rep_y)**2 + (j-rep_x)**2)
                if dist <=5:
                    mask[i,j] = 255 # Draw a point on the mask image
                    

# Display the mask image with points
cv2.imwrite('mask_point.png',mask)
cv2.imshow('Mask Image with Points', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()


















