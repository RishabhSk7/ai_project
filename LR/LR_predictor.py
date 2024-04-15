import joblib
from skimage.io import imread
from skimage.transform import resize
import os

Categories = os.listdir("OutputFiles/Moods and Moments")

model = joblib.load("LR/LR.pkl")

image = resize(imread("test.png"), (744, 554)).flatten().reshape(1, -1)

print(":", Categories[model.predict(image)[0]])
