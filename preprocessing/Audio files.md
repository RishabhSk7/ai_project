### Sampling
Audio sampling is the process of transforming a musical source into a digital file. Digital audio recording does this by taking samples of the audio source along the soundwaves at regular intervals. The more samples you take - known as the ‘sample rate’ - the more closely the final digital file will resemble the original. A higher sample rate tends to deliver a better-quality audio reproduction.

- usually recorded at 44.1kHz

### Bit depth
Every sample you take when making an audio recording needs to be stored within your computer’s ‘bits’. The more bits you use to record each sample, the better the sound reproduction.

### Frames
An audio frame, or sample, contains amplitude (loudness) information at that particular point in time. To produce sound, tens of thousands of frames are played in sequence to produce frequencies.
The size of an audio frame is **calculated by multiplying the sample size in bytes by the number of channels**.


### MP3 
MP3 is a popular format that stores audio data in a lossy format, i.e., it trades of some details in data for lower memory usage.
![[Pasted image 20240321200044.png]]
Mp3 stores data in 4 steps:
1. Divide audio singal into frames.
2. Each sample passes through a fast Fourier transform (fft), after which a psychoacoustic model is applied.
3. Each frame is then qunatified and encoded to follow the bitrate and other constraints.
4. Finally the bitstream is converted to audio frame which is 1152 samples each, and each sample has two granules each, of size 576 samples.


##### More about Encoding
With MP3, the sound samples are transformed using methods that involve Fourier Series Transformations. A frequency analysis of the sound is the basis for this transformation. Based on this frequency analysis, the sound is split into frequency bands, each band corresponding to a particular frequency range. With MP3, 32 frequency bands are used. Based on the frequency analysis, the encoder uses what is called a psycho-acoustic model to compute the significance of each band for the human perception of the sound. _The idea is that the the human ear can only discern sounds from 20Hz to 20KHz, so any data outside of this threshold can be discarded to make the file smaller.



### WAV FILE
WAV file are container files. 
They differ from mp3 in that while a MP3 file uses a special decoding to store data, a WAV file is just a container. It can store any kind of data which is usually in PCM encoding but not necessarily. The Type of encoding used is usually stored in the header of wav file. 

