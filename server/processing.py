import sys
import io
from PIL import Image

sys.path.append("/home/Sk7/Documents/python/ai_project")        #necessary else imports give a headache
from preprocessing.decoder import mp3_to_wav
from preprocessing.visualiser import audio_to_image
from NeuralNetwork.NN_predictor import predict as NN
from LR.LR_predictor import predict as LR
from SVM.SVM_predictor import predict as SVM

def image_processing(image: io.BytesIO, model: str):
    "predict the image data"

    if model=="MLP":
        genre = NN(Image.open(image))  #all predict functions use resize, and it only takes imread object
        # which in turn takes a filename, and cannot read from BytesIO directly
    elif model=="LR":
        genre = LR(Image.open(image))
    else:
        genre = SVM(Image.open(image))

    return genre

def audio_processing(audio: io.BytesIO, model: str):
    """Process audio to image, before forwarding to image processing"""
    if audio.read()[:4] == b"RIFF":
        audio.seek(0)       #since the cursor moved when reading first 4 words
        img = audio_to_image(audio, predicting=True)        #returns io.BufferIO
        return image_processing(img, model)

    else:
        audio.seek(0)
        audio = mp3_to_wav(audio)
        return audio_processing(audio, model)


if __name__ == "__main__":
    with open("test/test.mp3", "rb") as file:
        buf = io.BytesIO(file.read())
        print(audio_processing(buf, "SVM"))
