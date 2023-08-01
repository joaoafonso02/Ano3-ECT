import cv2
import mediapipe as mp
import numpy

def merge_options(arr1, arr2):
    for opts in arr2:
        if opts in arr1:
            arr1[opts] = arr2[opts]

def mediapipe_hand(videoPath, **user_options):
    options = {'static_image_mode':True,'max_num_hands':2,'min_detection_confidence':0.5}
    options = merge_options(options, user_options)

    mp_hands = mp.solutions.hands

    results = [] # vertices and edges

    with mp_hands.Hands(options) as hands:
        # cap = cv2.VideoCapture(videoPath)
        filestr = videoPath.read()
        file_bytes = numpy.fromstring(filestr, numpy.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # while cap.isOpened():
        #     ret, frame = cap.read()
        #     if not ret: break

        result = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if not result.multi_hand_landmarks: 
            return {'points': {'vertices': []}}

        for j in range(len(result.multi_hand_landmarks)):
            landmarks = result.multi_hand_landmarks[j].landmark
            results.append({
                'vertices': [{'x':i.x, 'y': i.y, 'z': i.z} for i in landmarks],
                'edges': [[0,1],[1,2],[2,3],[3,4],[0,5],[0,17],[5,6],[5,9],[6,7],[7,8],[9,10],[9,13],[10,11],[11,12],[13,14],[13,17],[14,15],[15,16],[17,18],[18,19],[19,20]]
            })
    
    resp = {
        'name': 'mediapipe_hands',
        'type': 'points',
        'points': results,
        'status': 'found'
    }

    return resp

def mediapipe_facedetection(videoPath, **user_options):
    options = {'model_selection':1, 'min_detection_confidence':0.5}
    merge_options(options, user_options)

    mp_face_detection = mp.solutions.face_detection

    results = [] # vertices and edges

    with mp_face_detection.FaceDetection(**options) as face_detection:
        filestr = videoPath.read()
        file_bytes = numpy.fromstring(filestr, numpy.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # while cap.isOpened():
        #     ret, frame = cap.read()
        #     if not ret: break

        result = face_detection.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if not result.detections: return {'points': {'vertices': []}}

        vertices = []
        edges = []
        for face in result.detections:
            i = len(vertices)
            box = face.location_data.relative_bounding_box
            vertices.append({'x': box.xmin, 'y': box.ymin})
            vertices.append({'x': box.xmin+box.width, 'y': box.ymin})
            vertices.append({'x': box.xmin, 'y': box.ymin+box.height})
            vertices.append({'x': box.xmin+box.width, 'y': box.ymin+box.height})
            edges += [[i,i+1],[i,i+2],[i+1,i+3],[i+2,i+3]]
            vertices += [{'x':j.x, 'y':j.y} for j in face.location_data.relative_keypoints]

        # location_data = result.detections[0].location_data
        # box_vertices = []
        # print(location_data)
        results.append({
            'vertices': vertices,
            'edges': edges,
        })
    
    resp = {
        'name': 'mediapipe_facedetection',
        'type': 'points',
        'points': results,
        'status': 'found'
    }

    return resp



def mediapipe_facemesh(videoPath, **user_options):
    options = {'static_image_mode':True,'max_num_faces':1,'refine_landmarks':True,'min_detection_confidence':0.5}
    merge_options(options, user_options)

    mp_facemesh = mp.solutions.face_mesh

    results = [] # vertices and edges

    with mp_facemesh.FaceMesh(**options) as face_mesh:
        filestr = videoPath.read()
        file_bytes = numpy.fromstring(filestr, numpy.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        result = face_mesh.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if not result.multi_face_landmarks: return

        vertices = []
        for face in result.multi_face_landmarks:
            # print(len(list(face.landmark)))
            vertices += [{'x': i.x, 'y': i.y, 'z': i.z} for i in face.landmark]

        results.append({
            'vertices': vertices,
            'edges': []
        })
    
    resp = {
        'name': 'mediapipe_facemesh',
        'type': 'points',
        'points': results,
        'status': 'found'
    }

    return resp

available = ['mediapipe_hand', 'mediapipe_facedetection', 'mediapipe_facemesh']

if __name__ == '__main__':
    pass
    # hand = mediapipe_hand(videoPath="./yeye.webm")

    # facedetection = mediapipe_facedetection(videoPath="./yeye.webm")

    # facemesh = mediapipe_facemesh(videoPath='./yeye.webm')

    # print(facemesh)