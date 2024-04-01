from wave import Wave_write
import mp3

def mp3_to_wav(name) -> None:
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