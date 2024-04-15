import os
import io
from typing import Union
# from statistics import mean
import librosa
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append("/home/Sk7/Documents/python/ai_project")

global in_loc, out_loc

def audio_to_image(name: Union[io.BytesIO, str], mood:str="Only pass if visualising dataset", predicting:bool=False) -> Union[io.BytesIO, None]:
    matplotlib.use("agg")
    """converts wav audio files with PCM encoding to images in hsv format"""

    if not predicting:      #run if converting dataset
        # your program will likely have crashed before, so you're starting again. Ensures you
        # do not repeat the whole process
        if os.path.isfile(out_loc+ mood + "/" + name + ".png"):
            return None

        if name[:2]=="r ":      #removing songs that do not match vibe filtered via changing file names
            return None

        print(name)

        y = librosa.load(in_loc+mood+"/"+name, mono=True, sr=44100)[0]

    else:
        y = librosa.load(name, mono=True, sr=44100)[0]   #name is just argument, it is actually fd in this case

    s = np.abs(librosa.stft(y))
    # The STFT function returns a matrix D[...,f,t], represents the frequency bin f at frame t of the
    # signal.
    # If we do np.abs(D[...,f,t]) it will give frequency data of frequency bin f at t.
    # np.angle(D[...,f,t]) will give the angle or timing signal at frequency bin f at time t.
    # Since we only need frequency data, we do np.abs there.
    # gpt: 9640e2dd-62f1-4048-af0f-9d2c01ae47b3
    # https://librosa.org/doc/latest/generated/librosa.stft.html#librosa.stft

    a = librosa.amplitude_to_db(s, ref=np.max)
    # print(a.shape)
    fig, ax = plt.subplots()

    # please note use of hsv below
    img = librosa.display.specshow(a, cmap='hsv', y_axis="log", x_axis="time", ax=ax)
    # By converting the amplitude spectrogram to a dB scale, the resulting spectrogram provides
    # a more perceptually relevant representation of the audio signal's frequency content. This
    # is because human perception of sound intensity is roughly logarithmic, and using a dB
    # scale better captures the relative loudness of different frequency components in the audio
    # signal. Additionally, dB scaling can help visualize both low-level details and high-level
    # structures in the audio signal across a wide dynamic range.

    # NOTE: WE dont want to show axis, just graph so hiding extra details below
    # ax.set_title(name + " Frequency chart, scaled to decible values.")
    # fig.colorbar(img, ax=ax, format="%+2.0f dB")b
    plt.axis("off")

    if not predicting:
        fig.savefig(
            out_loc + mood + "/" + name + ".png",
            bbox_inches="tight",
            transparent=True,
            pad_inches=0,
            dpi=150
        )

        # just for debugging
    else:
        img = io.BytesIO()
        fig.savefig(img, format="png")
        img.seek(0)
        return img

    plt.close(fig)                  #THIS LINE IS IMPORTANT
    # need to close the figure manually. Other wise memory usage increases.
    # del doesnt help, neither does gc.collect()
    return None

if __name__ == "__main__":
    in_loc = "Files/Moods and Moments/"
    out_loc = "OutputFiles/Moods and Moments/"
    if not os.path.exists(out_loc):
        os.mkdir(out_loc)

    for i in os.listdir(in_loc):
        PATH = in_loc+"/"+i
        print(PATH)
        print("\n\n\n")
        if not os.path.exists(out_loc+i):
            os.mkdir(out_loc + i)

        for j in os.listdir(PATH):
            audio_to_image(j, i)
