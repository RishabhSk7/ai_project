a### Step1:
Step 1 consists of downloading files. We first get all possible moods in the YTMUSIC service. Then we manually create a dict of these "moods" with a playlist for these moods and a url of such a playlist. We create manually because sure we could take input from terminal itself, but it is more intutive to rather use the YT music UI. Once we have this dict, we use yt_dlp library to download the audio files from the yt music service to locally.

### Step2:
As we download the files, we apply a post processor to the downloaded files. This post processor (in yt-dlp) uses ffmpeg to convert the webm file to wav files with PCM encoding and then deletes the original file. 
### Step3:
After that, we use stft transformation from the librosa library. The STFT represents a signal in the time-frequency domain by computing discrete Fourier transforms (DFT) over short overlapping windows. Further, computing `np.abs(D[..., f, t])` is the magnitude of frequency bin `f` at frame `t`. 
This magnitude of frequencies data is then normalised to loudness using amplitude_to_db function.

### Step4:
For visualising the data, we use `librosa.display.specshow`. The given function is used to Display a spectrogram/chromagram/cqt/etc. We use the "hsv" colour map to cover the whole rgb spectrum. The images are saved in "Files" and then each image is saved in its respective mood folder. 