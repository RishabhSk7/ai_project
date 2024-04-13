import joblib
from skimage.io import imread
from skimage.transform import resize

model = joblib.load("SVM/SVM.pkl")

image = resize(imread("test.png"), (744, 554)).flatten().reshape(1, -1)

print(model.predict(image))
