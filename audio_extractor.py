from pytubefix import YouTube
from pytubefix.cli import on_progress

base_dir = f"audios"
video_url= "https://www.youtube.com/watch?v=LgVpUDtk9fc"
yt = YouTube(video_url, on_progress_callback=on_progress)
caption = yt.captions['a.pt']
caption.save_captions("captions.txt")

stream_url = yt.streams.get_audio_only()
stream_url.download()

audio_path = f"{base_dir}/{yt.title}"
