import mediapipe as mp
from mediapipe import solutions
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2
import cv2 as cv
import numpy as np
import time, math

HANDEDNESS_MARGIN = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54) # vibrant green
RPS_TEXT_COLOR = (255, 0, 0) 
RPS_MARGIN = 40

def calc_distance(origen, destino):
    return math.sqrt((origen.x-destino.x)**2 + (origen.y-destino.y)**2 + (origen.z-destino.z)**2) 

def is_figner_up(finger_pip, finger_tip, wrist):
    dist_pip = calc_distance(wrist,finger_pip)
    dist_tip = calc_distance(wrist,finger_tip)

    return dist_tip > dist_pip

def draw_landmarks_on_image(rgb_image, detection_result):
    hand_landmarks_list = detection_result.hand_landmarks
    annotated_image = np.copy(rgb_image)
    
    # Loop through the detected hands to visualize.
    for idx in range(len(hand_landmarks_list)):
        rps = ""
        hand_landmarks = hand_landmarks_list[idx]

        # Create bool for each finger if its up (pip and tip) [see image]
        wrist = hand_landmarks_list[idx][0]
        index = is_figner_up(hand_landmarks_list[idx][6],
                            hand_landmarks_list[idx][8],
                            wrist)
        middle = is_figner_up(hand_landmarks_list[idx][10],
                            hand_landmarks_list[idx][12],
                            wrist)
        ring = is_figner_up(hand_landmarks_list[idx][14],
                            hand_landmarks_list[idx][16],
                            wrist)
        pinky = is_figner_up(hand_landmarks_list[idx][18],
                            hand_landmarks_list[idx][20],
                            wrist)

        if index and middle and ring and pinky: rps = "papel"
        elif index and middle: rps = "tijera"
        elif not index and not middle and not ring and not pinky: rps = "piedra"

        # Draw the hand landmarks.
        hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        hand_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
        ])
        solutions.drawing_utils.draw_landmarks(
              annotated_image,
              hand_landmarks_proto,
              solutions.hands.HAND_CONNECTIONS,
              solutions.drawing_styles.get_default_hand_landmarks_style(),
              solutions.drawing_styles.get_default_hand_connections_style())
    
        # Get the top left corner of the detected hand's bounding box.
        height, width, _ = annotated_image.shape
        x_coordinates = [landmark.x for landmark in hand_landmarks]
        y_coordinates = [landmark.y for landmark in hand_landmarks]
                
        # Draw rock, paper or scissor
        text_x = int(min(x_coordinates) * width) 
        text_y = int(min(y_coordinates) * height) - RPS_MARGIN
        cv.putText(annotated_image, f"{rps}",
                    (text_x, text_y), cv.FONT_HERSHEY_DUPLEX,
                    FONT_SIZE, HANDEDNESS_TEXT_COLOR, FONT_THICKNESS, cv.LINE_AA)
    
    return annotated_image

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='IA\Programacion\Ejercicios\piedra_papel_tijera\\model\hand_landmarker.task'),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=2)

cam = cv.VideoCapture(0) 
cv.namedWindow("Cam") 

with HandLandmarker.create_from_options(options) as landmarker:

    while cam.isOpened():  
        # Read frames from videoCaptura and show
        _, frame = cam.read() 
        cv.imshow("Cam", frame)

        # The landmarker is initialized. 
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        hand_landmarker_result = landmarker.detect_for_video(mp_image, int(round(time.time() * 100)))
        annotated_image = draw_landmarks_on_image(mp_image.numpy_view(), hand_landmarker_result)
        cv.imshow("Salida", annotated_image)

        # Press esc to exit
        if cv.waitKey(10) & 0xFF == 27: cam.release()
    
    cv.destroyAllWindows()