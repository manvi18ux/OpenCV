import os
import cv2 as cv
import numpy as np

people = ['imagef1', 'imagef2', 'imagef3']
DIR = r'C:\Users\sinha\Desktop\OpenCV\images'

haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            if not img.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue

            img_array = cv.imread(img_path)
            if img_array is None:
                print(f"Skipping unreadable file: {img_path}")
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

        print(f"{img_path} -> Faces detected: {len(faces_rect)}")

    for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

print("Training Done -----------------------")
print(f"Total features collected = {len(features)}")
print(f"Total labels collected   = {len(labels)}")

if len(features) == 0:
    raise Exception("❌ No faces detected! Check dataset or Haar cascade.")

labels = np.array(labels, dtype=np.int32)

# Train recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

# Save model (absolute path)
face_recognizer.save(r"C:\Users\sinha\Desktop\OpenCV\face_trained.yml")

# Save features & labels
np.save("features.npy", np.array(features, dtype="object"))
np.save("labels.npy", labels)
