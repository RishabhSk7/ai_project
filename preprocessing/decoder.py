from wave import Wave_write
import mp3
import io
import sys
sys.path.append("/home/Sk7/Documents/python/ai_project") 

def mp3_to_wav(name:str) -> None:
    """converts name arg to mp3 file to wav saves locally"""
    with open(name, "rb") as read_file, open("IG.wav", "wb") as write_file:

        decoder = mp3.Decoder(read_file)

        sample_rate = decoder.get_sample_rate()
        nchannels = decoder.get_channels()

        wav_file = Wave_write(write_file)
        wav_file.setnchannels(nchannels)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)

        while True:
            pcm_data = decoder.read(4000)

            if not pcm_data:
                break
            else:
                wav_file.writeframes(pcm_data)

def mp3_to_wav(file:io.BytesIO) -> io.BytesIO:
    """overlaoded function, for when you pass buffer object"""
    decoder = mp3.Decoder(file)

    sample_rate = decoder.get_sample_rate()
    nchannels = decoder.get_channels()

    a = io.BytesIO()
    wav_file = Wave_write(a)
    wav_file.setnchannels(nchannels)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)

    while True:
        pcm_data = decoder.read(4000)

        if not pcm_data:
            break
        else:
            wav_file.writeframes(pcm_data)

    a.seek(0)       #since we finished writing, cursor is at end of file
    return a

if __name__ == "__main__":
    with open("test/test.mp3", "rb") as file:
        audiofile = io.BytesIO(file.read())
        mp3_to_wav(audiofile)
