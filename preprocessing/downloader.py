import yt_dlp
import os
from ytmusicapi import YTMusic

ytmusic = YTMusic()
moods = ytmusic.get_mood_categories()
# pprint.pprint(moods)
# we'are using "moods and moments" instead of "genres"
for i in moods["Genres"]:
    print(i)
# Just printing the moods like "chill". You will have to hardcode the playlist dict

input()
# just wait to genres

##NOTE DO NOT use music.youtube.com, instead use www.youtube.com
playlists = {
    # "chill": "https://music.youtube.com/playlist?list=RDCLAK5uy_krbBs7P2iEb30IODyVbiOXWyhZtAIX9Uk",
    # "Party": "https://music.youtube.com/playlist?list=RDCLAK5uy_nlOMew8qv8HGXb9HbshuU1OgH3aL_JMKA",
    # "sad": "https://music.youtube.com/playlist?list=RDCLAK5uy_le5uB3137WE9n3TxANc_r8T3YM8QJlUvo",
    # "sleep": "https://music.youtube.com/playlist?list=RDCLAK5uy_ldLj_raotpFCQGWiQ7L-Ag5GTbGOyjgRY",
    # "workout": "https://music.youtube.com/playlist?list=PL7W9LuUf6bFrxSIjYqny-ac12v6P_2bP8",
}
# have a dict of custom playlists, in format genre:url


def download_playlist(genre, playlist):
    "downloads a playlist. Takes a 'mood' and 'playlist' url."

    # Define default path
    path = r"../Files/Moods and Moments/"+genre
    # create a playlist folder if not exist
    if os.path.exists(path):
        return
    
    os.mkdir(path)

    # Define download rate limit in byte
    ratelimit = 5000000

    # Define download format
    format= "mp3/wav/bestaudio/best"

    # Get url as argument
    url = playlist

    # Download all videos in a playlist
    ydl_opts = {
        "ignoreerrors": True,
        "abort_on_unavailable_fragments": True,
        "format": format,
        "outtmpl": path + "/%(title)s ## %(uploader)s ## %(id)s.%(ext)s",
        "ratelimit": ratelimit,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
    }

    # Downloads depending on the options set above
    if ydl_opts is not None:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)


for key, value in playlists.items():
    download_playlist(key, value)
