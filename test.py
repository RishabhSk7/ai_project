from pydub import AudioSegment
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

# song = AudioSegment.from_mp3("DNM.mp3")
# # print(song[:30*1000].raw_data)
# print(song.frame_count())
# print(song.frame_count(1))
# print(song.frame_width)
# print(len(song))
# print(song.frame_width*len(song))
# # 3840×2160

# song = AudioSegment.from_mp3("lf.mp3")
# sound = song.set_channels(1)
# fm = "lf_mono.wav"

song = AudioSegment.from_mp3("DNM.mp3")
samplerate = song.frame_count(1)*1000
song = song.split_to_mono()
# 0 index is left, 1 is right
data = np.array(song[0].get_array_of_samples())
print(f"Sample rate: {samplerate}")
# print(data)
length = data.shape[0] / samplerate
print(f"length = {length}s")

def extract_peak_frequency(d, sampling_rate):
    fft_data = np.fft.fft(d)
    freqs = np.fft.fftfreq(len(d))

    peak_coefficient = np.argmax(np.abs(fft_data))
    print("mean freq: ", np.mean(freqs) * sampling_rate)
    peak_freq = freqs[peak_coefficient]
    print(freqs)

    return abs(peak_freq * sampling_rate)

print(extract_peak_frequency(data, samplerate))
