# Code de détection de la bille (extrait et nettoyé)
import cv2  # Importing the opencv module
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import imutils
import math

# Show OpenCV version
print("OpenCV version : {0}".format(cv2.__version__))

# Choose video
cv2.namedWindow("preview")
filename = "C:\\Users\\Andy9\\Projet\\Video\\video7.MOV"

# Load video
cap = cv2.VideoCapture(filename)
print("Open file: ", filename)

# Get framerate
framerate = cap.get(cv2.CAP_PROP_FPS)
print("Framerate: ", framerate, "fps")

# Minimum required radius of enclosing circle of contour
MIN_RADIUS = 2

# RGB Color ranges for color detection
lower_red = np.array([170, 70, 50])
upper_red = np.array([180, 255, 255])
lower_green = np.array([30, 50, 50])
upper_green = np.array([90, 255, 255])


# Get width of image and rescale it
original_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
final_width = math.floor(original_width)

# Scale factor
scale_factor = 0.59 / 1765  # ( object’s size in real life (meters) ) / ( object’s size in pixels )
resize_factor = original_width / final_width
scale = scale_factor * resize_factor

# Creating a Pandas DataFrame to store data points
data_features = ['time', 'color', 'cx', 'cy']
data_pts = pd.DataFrame(data=None, columns=data_features, dtype=float)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:  # Infinite loop
    # Take frame
    success, img = cap.read()

    # Get time in seconds
    current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000

    # Break if video ends
    if not success:
        break

    img = imutils.resize(img, width=final_width)

    # Blur image to remove noise
    img_filter = cv2.GaussianBlur(img.copy(), (3, 3), 0)

    # Convert image from BGR to HSV
    img_filter = cv2.cvtColor(img_filter, cv2.COLOR_BGR2HSV)

    # Create masks for red and green balls
    mask_red = cv2.inRange(img_filter.copy(), lower_red, upper_red)
    mask_green = cv2.inRange(img_filter.copy(), lower_green, upper_green)

    # Dilate images to make white blobs larger
    mask_red = cv2.erode(mask_red, None, iterations=2)
    mask_red = cv2.dilate(mask_red, None, iterations=2)
    mask_green = cv2.erode(mask_green, None, iterations=2)
    mask_green = cv2.dilate(mask_green, None, iterations=2)

    # Process contours for each color
    for mask, color_name, color_display in [
        (mask_red, "red", (255, 255, 0)),
        (mask_green, "green", (0, 255, 0))]:
        
        contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        if contours:
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            if M["m00"] > 0 and radius >= MIN_RADIUS:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                # Save data points
                data_pts.loc[data_pts.size / len(data_features)] = [
                    current_time,
                    color_name,
                    center[0] * scale,
                    center[1] * scale
                ]
                # Draw a circle for the detected ball
                cv2.circle(img, center, int(round(radius)), color_display, 2)

    # Display the frame
    cv2.imshow('webcam', img)

    # Save the video with the position tracker
    out.write(img)

    # Quit if 'q' is pressed
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print("Total time: ", current_time)

# Close displaying windows
cap.release()
cv2.destroyAllWindows()

# Plot vertical positions as a function of time
plt.figure()
for color in ['red', 'green']:
    plt.plot(
        data_pts[data_pts['color'] == color]['time'],
        -data_pts[data_pts['color'] == color]['cx'],
        '.-',
        label=f'{color} ball')
    
plt.xlabel('time')
plt.ylabel('cx')
plt.legend()
plt.grid()
plt.show()

# Export data as CSV file
data_pts.to_csv('Video_RCG.csv', index=False)
