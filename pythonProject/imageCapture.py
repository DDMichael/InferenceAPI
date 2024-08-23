import cv2

# Open the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Cannot open webcam")
    exit()

# Adjust camera settings
cap.set(cv2.CAP_PROP_BRIGHTNESS, 1)  # Increase brightness (0 to 1)
cap.set(cv2.CAP_PROP_CONTRAST, 0.6)    # Increase contrast (0 to 1)
cap.set(cv2.CAP_PROP_EXPOSURE, -4)     # Set exposure (smaller values may help)

# Capture frame-by-frame
ret, frame = cap.read()

# If frame is read correctly ret is True
if not ret:
    print("Can't receive frame (stream end?). Exiting ...")
    cap.release()
    exit()

# Display the captured frame
# cv2.imshow('Captured Image', frame)

# Save the captured image
cv2.imwrite('captured_image.png', frame)

# Wait for a key press and then close the display window
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Release the webcam
cap.release()

print("Image has been captured")