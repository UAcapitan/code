
import os
import youtube_dl
import telebot


class YouTubeAudioDownloader:
    def __init__(self):
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
                'preferredquality': '192',
            }],
        }

        self.urls = []

        self.run()

    def input_urls(self):
        url = ''

        while url != 'q':
            url = input("> ")
            if url and url != 'q':
                self.urls.append(url)

    def download(self):
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            for url in self.urls:
                if self.check_type_and_filesize(ydl, url):
                    try:
                        ydl.download([url])
                    except:
                        continue

    def check_type_and_filesize(self, ydl, url):
        info = ydl.extract_info(url, download=False)
        formats = info['formats']
        n = [f["filesize"] for _, f in enumerate(formats) if f["ext"] == "m4a"]
        print(n)
        if n:
            if round(n[0] / 1048576) >= 50:
                return False
        else:
            return False
        return True

    def send_to_group(self):
        bot = telebot.TeleBot("5489279030:AAEZ-w5vJ5FYPLcHEVyLg0lkM5wDEQne2y8", parse_mode=None)
        for file in os.listdir():
            if 'm4a' in file:
                try:
                    bot.send_audio(chat_id=-835507366, audio=open(file, 'rb'))
                except:
                    print("Error during uploading")
                os.remove(file)
            if "webp" in file:
                os.remove(file)

    def run(self):
        self.input_urls()
        self.download()

        if self.urls_another_type:
            self.download_another_type()

        self.send_to_group()


if __name__ == "__main__":
    app = YouTubeAudioDownloader()
