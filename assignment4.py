import cv2
import numpy as np

image_path = input("Enter the path to your image: ")
image = cv2.imread(image_path)
if image is None:
    print("Could not read the image. Check the path.")
    exit()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blurred, 50, 150)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

def detect_shape(contour):
   
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * peri, True)
    vertices = len(approx)
    
    if vertices == 3:
        return "Triangle"
    elif vertices == 4:
        
        x, y, w, h = cv2.boundingRect(approx)
        ar = w / float(h)
        return "Square" if 0.95 <= ar <= 1.05 else "Rectangle"
    elif vertices == 5:
        return "Pentagon"
    elif vertices == 6:
        return "Hexagon"
    else:
        
        area = cv2.contourArea(contour)
        if area == 0:
            return "Unknown"
        circularity = (4 * np.pi * area) / (peri * peri)
        return "Circle" if circularity > 0.8 else "Ellipse/Other"

for contour in contours:
    shape = detect_shape(contour)
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.putText(image, shape, (cX - 40, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

cv2.imshow("Contours and Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
