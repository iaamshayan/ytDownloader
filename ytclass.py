import yt_dlp

class ytDownloader:
    def __init__(self, link):
        try:
            if ("youtube.com/watch?v=" not in link) and ("youtu.be/" not in link):
                raise ValueError("Invalid YouTube link.")
            else:
                self.link = link
                self.video_info = self._get_video_info()
        except Exception as e:
            print("Error:", e)
            self.video_info = None

    def _get_video_info(self):
        try:
            with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                return ydl.extract_info(self.link, download=False)
        except Exception as e:
            print("Failed to fetch video info:", e)
            return None

    def get_title(self):
        return self.video_info.get('title') if self.video_info else "N/A"

    def get_views(self):
        return self.video_info.get('view_count') if self.video_info else "N/A"

    def download_video(self, path=''):
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{path}/%(title)s.%(ext)s'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.link])

    def download_audio(self, path=''):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.link])

    def display_info(self):
        if self.video_info:
            print("Title:", self.get_title())
            print("Views:", self.get_views())
        else:
            print("No valid YouTube info available.")
