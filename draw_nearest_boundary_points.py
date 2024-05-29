# import cv2
# import numpy as np
# from shapely.geometry import Polygon, Point

# def find_nearest_boundary_points(contours, mask):
#     for cnt in contours:
#         if len(cnt) >= 4:  # Filter out contours with less than 4 points
#             # Convert contour to a Shapely Polygon
#             points = [Point(coord[0][0], coord[0][1]) for coord in cnt]
#             polygon = Polygon([[p.x, p.y] for p in points])

#             # Find the center point using representative point method
#             rep_point = polygon.representative_point()
#             cX, cY = int(rep_point.x), int(rep_point.y)
#             upper_point = (cX, np.argmax(mask[:cY, cX][::-1] != 0))
#             lower_point = (cX, cY + np.argmax(mask[cY:, cX] != 0))
#             left_point = (np.argmax(mask[cY, :cX][::-1] != 0), cY)
#             right_point = (cX + np.argmax(mask[cY, cX:] != 0), cY)

#             # Draw the boundary points on the original mask image
#             cv2.circle(mask, upper_point, 3, 255, -1)
#             cv2.circle(mask, lower_point, 3, 255, -1)
#             cv2.circle(mask, left_point, 3, 255, -1)
#             cv2.circle(mask, right_point, 3, 255, -1)

#     return mask



# image_path = '/home/usama/Median_erode__contours_low__and_high_resolution_test/centre_based_removing_Contour_logic_results/Failure_Cases_Centre_based_logic/demo117_4.jpg'
# mask = cv2.imread(image_path)

# result_mask_binary = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)[1]

# # Convert result_mask_binary to CV_8UC1 format
# result_mask_binary = cv2.cvtColor(result_mask_binary, cv2.COLOR_BGR2GRAY)

# # Finding contours directly from the binary mask
# contours, _ = cv2.findContours(result_mask_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# mask_with_points = find_nearest_boundary_points(contours, mask)

# cv2.imshow("Mask with Points", cv2.resize(mask_with_points, (800, 900)))
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite("filtered_image.png",mask_with_points)



# import cv2
# import numpy as np
# from scipy.spatial import distance
# from shapely.geometry import Polygon, Point
    
    
# sample_img = cv2.imread("/home/usama/Median_erode__contours_low__and_high_resolution_test/centre_based_removing_Contour_logic_results/Failure_Cases_Centre_based_logic/demo117_4.jpg")
    
# # convert to black and white color space
# sample_img_grey = cv2.cvtColor(sample_img, cv2.COLOR_BGR2GRAY)
# contours, hierarchy = cv2.findContours(sample_img_grey, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# #find center of image and draw it (blue circle)
# image_center = np.asarray(sample_img_grey.shape) / 2
# image_center = tuple(image_center.astype('int32'))
# cv2.circle(sample_img, image_center, 3, (255, 100, 0), 2)

# buildings = []
# for contour in contours:
#     # find center of each contour
#     M = cv2.moments(contour)
#     if len(contour) >= 4:  # Filter out contours with less than 4 points
#         # Convert contour to a Shapely Polygon
#         points = [Point(coord[0][0], coord[0][1]) for coord in contour]
#         polygon = Polygon([[p.x, p.y] for p in points])

#         # Find the representative point of the polygon (centroid)
#         rep_point = polygon.representative_point()

#         contour_center = (int(rep_point.x), int(rep_point.y))
#         # calculate distance to image_center
#         distances_to_center = (distance.euclidean(image_center, contour_center))

#         # save to a list of dictionaries
#         buildings.append({'contour': contour, 'center': contour_center, 'distance_to_center': distances_to_center})

#         # draw each contour (red)
#         cv2.drawContours(sample_img, [contour], 0, (0, 50, 255), 2)
#         M = cv2.moments(contour)

#         # draw center of contour (green)
#         cv2.circle(sample_img, contour_center, 3, (100, 255, 0), 2)

# # sort the buildings
# sorted_buildings = sorted(buildings, key=lambda i: i['distance_to_center'])

# # find contour of closest building to center and draw it (blue)
# center_building_contour = sorted_buildings[0]['contour']
# cv2.drawContours(sample_img, [center_building_contour], 0, (255, 0, 0), 2)
# cv2.imwrite("sample_image.jpg",sample_img)
# cv2.imshow("Image", sample_img)
# cv2.waitKey(0)



# import cv2
# import numpy as np
# from scipy.spatial import distance
# from shapely.geometry import Polygon, Point

# sample_img = cv2.imread("/home/usama/Median_erode__contours_low__and_high_resolution_test/centre_based_removing_Contour_logic_results/Failure_Cases_Centre_based_logic/demo117_4.jpg")

# # convert to black and white color space
# sample_img_grey = cv2.cvtColor(sample_img, cv2.COLOR_BGR2GRAY)
# contours, hierarchy = cv2.findContours(sample_img_grey, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # find center of image and draw it (blue circle)
# image_center = np.asarray(sample_img_grey.shape) / 2
# image_center = tuple(image_center.astype('int32'))
# cv2.circle(sample_img, image_center, 3, (255, 100, 0), 2)

# buildings = []
# for contour in contours:
#     # find center of each contour
#     M = cv2.moments(contour)
#     if len(contour) >= 4:  # Filter out contours with less than 4 points
#         # Convert contour to a Shapely Polygon
#         points = [Point(coord[0][0], coord[0][1]) for coord in contour]
#         polygon = Polygon([[p.x, p.y] for p in points])

#         # Find the representative point of the polygon (centroid)
#         rep_point = polygon.representative_point()

#         contour_center = (int(rep_point.x), int(rep_point.y))
#         # calculate distance to image_center
#         distances_to_center = (distance.euclidean(image_center, contour_center))

#         # save to a list of dictionaries
#         buildings.append({'contour': contour, 'center': contour_center, 'distance_to_center': distances_to_center})

#         # draw each contour (red) if distance is greater than or equal to 5 pixels
#         if distances_to_center < 200:
#             cv2.drawContours(sample_img, [contour], 0, (0, 50, 255), 2)
#             # draw center of contour (green)
#             cv2.circle(sample_img, contour_center, 3, (100, 255, 0), 2)

# # sort the buildings
# sorted_buildings = sorted(buildings, key=lambda i: i['distance_to_center'])

# # find contour of closest building to center and draw it (blue)
# center_building_contour = sorted_buildings[0]['contour']
# cv2.drawContours(sample_img, [center_building_contour], 0, (255, 0, 0), 2)

# cv2.imwrite("sample_image.jpg", sample_img)
# cv2.imshow("Image", sample_img)
# cv2.waitKey(0)


# import cv2
# import numpy as np
# from shapely.geometry import Polygon, Point

# sample_img = cv2.imread("/home/usama/Median_erode__contours_low__and_high_resolution_test/centre_based_removing_Contour_logic_results/Failure_Cases_Centre_based_logic/demo117_4.jpg")

# # convert to black and white color space
# sample_img_grey = cv2.cvtColor(sample_img, cv2.COLOR_BGR2GRAY)
# contours, hierarchy = cv2.findContours(sample_img_grey, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # find center of image and draw it (blue circle)
# image_center = np.asarray(sample_img_grey.shape) / 2
# image_center = tuple(image_center.astype('int32'))
# cv2.circle(sample_img, image_center, 3, (255, 100, 0), 2)

# buildings = []
# for contour in contours:
#     # find center of each contour
#     if len(contour) >= 4:  # Filter out contours with less than 4 points
#         # Convert contour to a Shapely Polygon
#         points = [Point(coord[0][0], coord[0][1]) for coord in contour]
#         polygon = Polygon([[p.x, p.y] for p in points])

#         # Find the representative point of the polygon (centroid)
#         rep_point = polygon.representative_point()

#         contour_center = (int(rep_point.x), int(rep_point.y))

#         # draw circles around the center of about 7 pixels distance
#         for i in range(-7, 8):
#             for j in range(-7, 8):
#                 if abs(i) + abs(j) < 5:  # check if the distance is within 7 pixels
#                     cv2.circle(sample_img, (contour_center[0] + i, contour_center[1] + j), 1, (0, 255, 0), -1)

# # draw each contour (red)
# cv2.drawContours(sample_img, contours, -1, (0, 50, 255), 2)

# cv2.imwrite("sample_image.jpg", sample_img)
# cv2.imshow("Image", sample_img)
# cv2.waitKey(0)




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
                    
        
        # Calculate Euclidean distance from representative point
        for i in range(mask.shape[0]):
            for j in range(mask.shape[1]):
                dist = np.sqrt((i - rep_y) ** 2 + (j - rep_x) ** 2)
                if dist <= 5:
                    mask[i, j] = 255  # Draw a point on the mask image

# Display the mask image with points
cv2.imwrite('mask_point.png',mask)
cv2.imshow('Mask Image with Points', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()


















