import os

from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import VIDEOS_LIST_DIR
from yt_concate.settings import CAPTIONS_SOURCE_DIR
from yt_concate.settings import CAPTIONS_CONVERTED_DIR


class Utils:
    def __init__(self):
        pass

    def create_dirs(self):  # yt-dlp原本就有這個功能...
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_LIST_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_SOURCE_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_CONVERTED_DIR, exist_ok=True)

    def get_video_list_file_path(self, channel_id):
        return os.path.join(VIDEOS_LIST_DIR, channel_id + '.txt')

    def check_video_list_file_exists(self, channel_id):
        path = self.get_video_list_file_path(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('=')[-1]

    def get_caption_files_path(self, url):
        return os.path.join(CAPTIONS_SOURCE_DIR, self.get_video_id_from_url(url))  # self.get_video_id_from_url(url) --->ID

    def check_caption_file_exists(self, url):
        path = self.get_caption_files_path(
            url) + '.en.srt'  # 檔案本體的路徑，加上後面的.en.srt是因為檔名就是長這樣，如果沒有加上的話就會沒有讀取到，程式會視為"沒有這個檔案"。
        return os.path.exists(path) and os.path.getsize(path) > 0

    def convert_caption_2_txt(self,video_id, video_id_caption):
        with open(os.path.join(CAPTIONS_CONVERTED_DIR, video_id + '.txt'), 'w', encoding='utf-8') as f:
            for line in video_id_caption:
                if line == 'caption':
                    continue
                f.write(line + ''.rjust(8, ' ')+ video_id_caption[line] + '\n')