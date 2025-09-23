import os

from yt_concate.settings import CAPTIONS_SOURCE_DIR
from yt_concate.settings import VIDEOS_SOURCE_DIR


class Youtube:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id_from_url(self.url)
        self.caption_files_path = self.get_caption_files_path()
        self.videos_id_dir = self.videos_id_dir()
        self.trimmed_videos_dir = self.trimmed_videos_dir()
        self.video_files_path = self.get_video_files_path()

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('=')[-1]

    def get_caption_files_path(self):
        return os.path.join(CAPTIONS_SOURCE_DIR, self.id)

    def get_video_files_path(self):
        return os.path.join(self.videos_id_dir, self.id + '.mp4')

    def videos_id_dir(self):
        return os.path.join(VIDEOS_SOURCE_DIR, self.id)

    def create_videos_id_dir(self):
        os.makedirs(self.videos_id_dir, exist_ok=True)

    def trimmed_videos_dir(self):
        return os.path.join(self.videos_id_dir, 'trimmed')

    def create_trimmed_videos_dir(self):
        os.makedirs(self.trimmed_videos_dir, exist_ok=True)

    def __str__(self):
        return '<Youtube(' + str(self.id) + ')>'

    def __repr__(self):
        content = ' || '.join([
            'id=' + str(self.id),
            'caption_files_path=' + str(self.caption_files_path),
            'video_files_path=' + str(self.video_files_path)
        ])
        return '<TargetCaptions(' + content + ')>'
