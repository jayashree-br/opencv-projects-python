import cv2
import numpy as np


# =========================
# Transformation Functions
# =========================

def resize_image(img, width, height):
    return cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)


def translate_image(img, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))


def rotate_image(img, angle):
    h, w = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(img, M, (w, h), borderMode=cv2.BORDER_REFLECT)


def scale_image(img, fx, fy):
    return cv2.resize(img, None, fx=fx, fy=fy, interpolation=cv2.INTER_AREA)


def affine_transform(img):
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv2.getAffineTransform(pts1, pts2)
    return cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))


def perspective_transform(img):
    h, w = img.shape[:2]
    pts1 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
    pts2 = np.float32([[0, 0], [w-100, 50], [50, h-100], [w, h]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    return cv2.warpPerspective(img, M, (w, h))


# =========================
# User Choice
# =========================

print("1.Resize 2.Translate 3.Rotate 4.Scale 5.Affine 6.Perspective 7.Flip")
option = int(input("Choose option: "))

width = height = x = y = angle = fx = fy = flip_code = None

if option == 1:
    width = int(input("Width: "))
    height = int(input("Height: "))
elif option == 2:
    x = int(input("Translate X: "))
    y = int(input("Translate Y: "))
elif option == 3:
    angle = int(input("Angle: "))
elif option == 4:
    fx = float(input("Scale fx: "))
    fy = float(input("Scale fy: "))
elif option == 7:
    flip_code = int(input("Flip code (0,1,-1): "))


# =========================
# Video Capture
# =========================

url = 0  # Use 0 for webcam or replace with video file path
cap = cv2.VideoCapture(url)

writer = None


# =========================
# Main Loop
# =========================

while True:

    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Original", cv2.resize(frame, (frame.shape[1]//2, frame.shape[0]//2), interpolation=cv2.INTER_AREA))

    # Apply transformation
    if option == 1:
        transformed = resize_image(frame, width, height)
        name = "Resized"

    elif option == 2:
        transformed = translate_image(frame, x, y)
        name = "Translated"

    elif option == 3:
        transformed = rotate_image(frame, angle)
        name = "Rotated"

    elif option == 4:
        transformed = scale_image(frame, fx, fy)
        name = "Scaled"

    elif option == 5:
        transformed = affine_transform(frame)
        name = "Affine"

    elif option == 6:
        transformed = perspective_transform(frame)
        name = "Perspective"

    elif option == 7:
        transformed = cv2.flip(frame, flip_code)
        name = "Flipped"

    else:
        print("Invalid option")
        break


    # Initialize writer once
    if writer is None:
        h, w = transformed.shape[:2]
        writer = cv2.VideoWriter(
            "assests/transformed_video.mp4",
            cv2.VideoWriter_fourcc(*'mp4v'),
            20,
            (w, h)
        )


    writer.write(transformed)
    cv2.imshow(name, cv2.resize(transformed, (w//2, h//2), interpolation=cv2.INTER_AREA))


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# =========================
# Cleanup
# =========================

cap.release()

if writer:
    writer.release()

cv2.destroyAllWindows()
