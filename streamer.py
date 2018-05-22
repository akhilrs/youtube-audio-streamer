import pafy
import vlc

video_url = 'https://www.youtube.com/watch?v=oh2LWWORoiM'
video = pafy.new(video_url)

best_media = video.getbestaudio()

print(best_media.url)

vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new(best_media.url)
player.play();