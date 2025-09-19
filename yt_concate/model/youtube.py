import os

from yt_concate.settings import CAPTIONS_SOURCE_DIR
from yt_concate.settings import VIDEOS_SOURCE_DIR


# from yt_concate.settings import VIDEOS_ORIGINAL_DIR
# from yt_concate.settings import VIDEOS_TRIMMED_DIR


class Youtube:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id_from_url(self.url)
        self.caption_files_path = self.get_caption_files_path()
        self.video_files_path = self.get_video_files_path()

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('=')[-1]

    def get_caption_files_path(self):
        return os.path.join(CAPTIONS_SOURCE_DIR, self.id)

    def get_video_files_path(self):
        VIDEOS_ID_DIR = os.path.join(VIDEOS_SOURCE_DIR, self.id)
        return os.path.join(VIDEOS_ID_DIR, self.id + '.mp4')

    def create_video_id_dir(self):
        VIDEOS_ID_DIR = os.path.join(VIDEOS_SOURCE_DIR, self.id)
        os.makedirs(VIDEOS_ID_DIR, exist_ok=True)

    def __str__(self):
        return '<Youtube(' + str(self.id) + ')>'

    def __repr__(self):
        content = ' || '.join([
            'id=' + str(self.id),
            'caption_files_path=' + str(self.caption_files_path),
            'video_files_path=' + str(self.video_files_path)
        ])
        return '<TargetCaptions(' + content + ')>'

    # def get_video_original_files_path(self):
    #     return os.path.join(VIDEOS_ORIGINAL_DIR, self.id)
    #
    # def get_video_trimmed_files_path(self):
    #     return os.path.join(VIDEOS_TRIMMED_DIR, self.id) #初步先這樣，檔名應該還要改還沒想到。
