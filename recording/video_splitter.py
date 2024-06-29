import cv2
import os

FILENAME = "scans"
FORMAT = "avi"

SKIP_FRAMES = 2
ROTATE_180 = False

ROOT_FOLDER = "D:/dataset"

capture = cv2.VideoCapture(f"{ROOT_FOLDER}/data/{FILENAME}.{FORMAT}")

frame_number = 0

if not os.path.isdir(f"{ROOT_FOLDER}/data/{FILENAME}"):
    os.makedirs(f"{ROOT_FOLDER}/data/{FILENAME}", exist_ok=True)

skipped = SKIP_FRAMES

while True:
    success, frame = capture.read()

    if success:
        if skipped < SKIP_FRAMES:
            skipped = skipped + 1
            continue
        else:
            skipped = 0

        if frame.shape[0] != 1080:
            frame = cv2.resize(frame, (1920, 1080), interpolation = cv2.INTER_AREA)
        if ROTATE_180:
            frame = cv2.rotate(frame, cv2.ROTATE_180)
        cv2.imwrite(f"{ROOT_FOLDER}/data/{FILENAME}/scan_{frame_number:05d}.jpg", frame)

    else:
        break

    frame_number = frame_number + 1

capture.release()