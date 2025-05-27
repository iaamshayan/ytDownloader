from pytube import YouTube

link = "https://www.youtube.com/watch?v=k1ka2tITfkU"
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)


print("*************************")
x = int(input("1 for video , 2 for audio download:: "))
if x == 1:
    yd = yt.streams.get_highest_resolution()
    yd.download('D:\Python\Projects\YTdownloader\YTfolder')
elif x==2:
    yd = yt.streams.get_audio_only()
    yd.download('D:\Python\Projects\YTdownloader\YTaudio')