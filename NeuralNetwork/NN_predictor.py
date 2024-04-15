import joblib
from PIL import Image
from skimage.transform import resize
import os
import numpy as np
import io

def predict(image: io.BytesIO):
    "predict image data using neural model"
    Categories = os.listdir("OutputFiles/Moods and Moments")

    model = joblib.load("NeuralNetwork/NN.pkl")
    image = image.resize((744, 554))

    # Convert the resized image to a numpy array
    image = np.array(image)

    # Flatten and reshape the resized image
    image = image.flatten().reshape(1, -1)
    return Categories[model.predict(image)[0]]


if __name__ == "__main__":
    print(predict(Image.open("test/test.png")))
