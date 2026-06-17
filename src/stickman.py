import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Pose & Hands
mp_pose = mp.solutions.pose
mp_hands = mp.solutions.hands
pose = mp_pose.Pose()
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

# Set up webcam
cap = cv2.VideoCapture(0)

# Stickman connection points for body
POSE_CONNECTIONS = mp_pose.POSE_CONNECTIONS

# Colors
BODY_COLOR = (0, 255, 0)
HAND_COLOR = (255, 0, 0)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    canvas = np.ones_like(frame) * 255  # white canvas

    # Convert to RGB
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process pose and hands
    pose_result = pose.process(img_rgb)
    hands_result = hands.process(img_rgb)

    # Draw pose stickman
    if pose_result.pose_landmarks:
        lm = pose_result.pose_landmarks.landmark
        for connection in POSE_CONNECTIONS:
            start_idx, end_idx = connection
            x1, y1 = int(lm[start_idx].x * w), int(lm[start_idx].y * h)
            x2, y2 = int(lm[end_idx].x * w), int(lm[end_idx].y * h)
            cv2.line(canvas, (x1, y1), (x2, y2), BODY_COLOR, 4)
        for l in lm:
            cx, cy = int(l.x * w), int(l.y * h)
            cv2.circle(canvas, (cx, cy), 5, BODY_COLOR, -1)

    # Draw hand stickman
    if hands_result.multi_hand_landmarks:
        for hand_landmarks in hands_result.multi_hand_landmarks:
            for connection in mp_hands.HAND_CONNECTIONS:
                start_idx, end_idx = connection
                x1, y1 = int(hand_landmarks.landmark[start_idx].x * w), int(hand_landmarks.landmark[start_idx].y * h)
                x2, y2 = int(hand_landmarks.landmark[end_idx].x * w), int(hand_landmarks.landmark[end_idx].y * h)
                cv2.line(canvas, (x1, y1), (x2, y2), HAND_COLOR, 2)
            for point in hand_landmarks.landmark:
                cx, cy = int(point.x * w), int(point.y * h)
                cv2.circle(canvas, (cx, cy), 3, HAND_COLOR, -1)

    # Display
    cv2.imshow("Stickman Mirror - DAEMON Mode", canvas)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()