import cv2
import numpy as np
from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt

# # Load mask image
# mask_image = cv2.imread('/home/usama/Median_erode__contours_low__and_high_resolution_test/centre_based_removing_Contour_logic_results/Failure_Cases_Centre_based_logic/demo117_4.jpg', 0)

# # Find contours
# contours, _ = cv2.findContours(mask_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Convert contours to polygons and determine representative points
# polygons = []
# representative_points = []

# for contour in contours:
#     if len(contour)>=4:
#         # Convert contour to Shapely Polygon
#         polygon = Polygon(contour.reshape(-1, 2))
#         polygons.append(polygon)
        
#         # Calculate representative point (centroid)
#         representative_point = polygon.representative_point()
#         representative_points.append(representative_point)

# # Function to find nearest boundary points
# # def find_nearest_boundary_points(polygon, representative_point):
# #     distances = []
# #     for point in polygon.exterior.coords[:-1]:  # Last point is the same as the first
# #         distances.append((point, representative_point.distance(Point(point))))
# #     distances.sort(key=lambda x: x[1])
# #     return distances[:4]  # Nearest 4 boundary points



# def find_nearest_boundary_points(polygon, representative_point):
#     distances = []
#     # Iterate over each interior ring
#     for interior in polygon.interiors:
#         for point in interior.coords[:-1]:  # Last point is the same as the first
#             distances.append((point, representative_point.distance(Point(point))))
#     distances.sort(key=lambda x: x[1])
#     return distances[:4]  # Nearest 4 boundary points


# # Draw circles on nearest boundary points
# result_image = cv2.cvtColor(mask_image, cv2.COLOR_GRAY2BGR)
# for polygon, representative_point in zip(polygons, representative_points):
#     nearest_points = find_nearest_boundary_points(polygon, representative_point)
#     for point, _ in nearest_points:
#         cv2.circle(result_image, (int(point[0]), int(point[1])), 5, (0, 255, 0), -1)

# # Visualize result
# cv2.imwrite("poit_respect_rep.jpg",result_image)
# plt.imshow(result_image)
# plt.axis('off')
# plt.show()



import cv2
import numpy as np
from shapely.geometry import Polygon, Point


# Load mask image
mask_image = cv2.imread('/home/usama/Median_erode__contours_low__and_high_resolution_test/centre_based_removing_Contour_logic_results/Failure_Cases_Centre_based_logic/demo117_4.jpg', 0)
_,mask_image = cv2.threshold(mask_image,25,255,cv2.THRESH_BINARY)
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


# def find_nearest_boundary_points(polygon, representative_point):
#     distances = []
#     # Iterate over each boundary point of the polygon's exterior ring
#     for point in polygon.exterior.coords[:-1]:  # Last point is the same as the first
#         distances.append((point, representative_point.distance(Point(point))))
#     distances.sort(key=lambda x: x[1])
#     return distances[:4]  # Nearest 4 boundar


def find_nearest_boundary_points(polygon, representative_point):
    # Extracting the coordinates of the representative point
    rep_x, rep_y = representative_point.x, representative_point.y
    
    # Extracting the coordinates of the polygon's exterior ring
    exterior_coords = list(polygon.exterior.coords[:-1])  # Last point is the same as the first
    
    # Initialize lists to store distances in each direction
    up_distances, down_distances, left_distances, right_distances = [], [], [], []
    
    # Iterate over each boundary point of the polygon's exterior ring
    for point in exterior_coords:
        # Calculate the distances in each direction
        x, y = point
        up_distances.append((point, rep_y - y))  # Distance in the up direction
        down_distances.append((point, y - rep_y))  # Distance in the down direction
        left_distances.append((point, rep_x - x))  # Distance in the left direction
        right_distances.append((point, x - rep_x))  # Distance in the right direction
        
    # Sort the distances in each direction
    up_distances.sort(key=lambda x: x[1])
    down_distances.sort(key=lambda x: x[1])
    left_distances.sort(key=lambda x: x[1])
    right_distances.sort(key=lambda x: x[1])
    
    # Return the nearest boundary points in each direction
    nearest_points = {
        "up": up_distances[0][0],
        "down": down_distances[0][0],
        "left": left_distances[0][0],
        "right": right_distances[0][0]
    }
    
    return nearest_points


# Draw circles on nearest boundary points
result_image = cv2.cvtColor(mask_image, cv2.COLOR_GRAY2BGR)
for polygon, representative_point in zip(polygons, representative_points):
    nearest_points = find_nearest_boundary_points(polygon, representative_point)
    for direction, point in nearest_points.items():
        cv2.circle(result_image, (int(point[0]), int(point[1])), 1, (0, 0, 255), -1)  # Red circles

# Display and save result
cv2.imwrite("demo_117_filled_contours.png", result_image)
cv2.imshow('Result', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
