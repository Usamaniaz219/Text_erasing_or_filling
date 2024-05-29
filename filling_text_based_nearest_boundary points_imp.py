import cv2
import numpy as np
from shapely.geometry import Polygon, Point

# Load mask image
mask_image = cv2.imread('/home/usama/Median_erode__contours_low__and_high_resolution_test/LUV__low_res_Meanshift_Bandwidth_8_data/New_results/demo123/demo123_15.jpg', 0)
_, mask_image = cv2.threshold(mask_image, 25, 255, cv2.THRESH_BINARY)

# Find contours with hierarchy
contours, hierarchy = cv2.findContours(mask_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Convert contours to polygons and determine representative points
polygons = []
representative_points = []

# Function to convert contours to polygons
def contour_to_polygon(contour):
    if len(contour) >= 4:
        return Polygon(contour.reshape(-1, 2))
    else:
        return None

# Convert child contours to polygons and find representative points
for idx in range(len(contours)):
    if hierarchy[0][idx][3] != -1:  # Child contour
        polygon = contour_to_polygon(contours[idx])
        if polygon:
            polygons.append(polygon)
            representative_points.append(polygon.representative_point())


def find_nearest_boundary_points(polygon, representative_point):
    # Extracting the coordinates of the representative point
    rep_x, rep_y = representative_point.x, representative_point.y

    # Extracting the boundary points of the polygon
    boundary_points = np.array(polygon.exterior.coords)

    # Initialize lists to store distances
    distances = []

    # Iterate over each boundary point of the polygon
    for point in boundary_points:
        # Calculate the distance between the representative point and each boundary point
        x, y = point
        distance = np.sqrt((rep_x - x) ** 2 + (rep_y - y) ** 2)
        distances.append((point, distance))

    # Sort the distances and return the nearest boundary point
    distances.sort(key=lambda x: x[1])
    return distances[0][0]


result_image = cv2.cvtColor(mask_image, cv2.COLOR_GRAY2BGR)
for polygon, representative_point in zip(polygons, representative_points):
    nearest_point = find_nearest_boundary_points(polygon, representative_point)
    nearest_point = tuple(map(int, nearest_point))

    # Extract the coordinates of the polygon's exterior ring and convert them to integer type
    exterior_coords_int = np.array([nearest_point, representative_point.coords[0]], dtype=np.int32)

    # Fill the closed region with white color
    cv2.fillPoly(result_image, [exterior_coords_int], (255, 255, 255))

# Display and save result
cv2.imwrite("demo123_15_filled_contours__2.png",result_image )
cv2.imshow('Result', cv2.resize(result_image, (900, 900)))
cv2.waitKey(0)
cv2.destroyAllWindows()
