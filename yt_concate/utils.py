import os

from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import VIDEOS_SOURCE_DIR
# from yt_concate.settings import VIDEOS_ORIGINAL_DIR
# from yt_concate.settings import VIDEOS_TRIMMED_DIR
from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import VIDEOS_LIST_DIR
from yt_concate.settings import CAPTIONS_SOURCE_DIR
from yt_concate.settings import CAPTIONS_CONVERTED_DIR
from yt_concate.settings import OUTPUTS_DIR


class Utils:
    def __init__(self):
        pass

    def create_dirs(self):  # yt-dlp原本就有這個功能...
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_LIST_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_SOURCE_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_SOURCE_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_CONVERTED_DIR, exist_ok=True)
        os.makedirs(OUTPUTS_DIR, exist_ok=True)

    def get_video_list_file_path(self, channel_id):
        return os.path.join(VIDEOS_LIST_DIR, channel_id + '.txt')

    def get_output_file_path(self, channel_id, search_word):
        filename = channel_id + '_' + search_word + '.mp4'
        return os.path.join(OUTPUTS_DIR, filename)

    def check_video_list_file_exists(self, channel_id):
        path = self.get_video_list_file_path(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def check_caption_file_exists(self, yt):  # ♥
        filepath = yt.caption_files_path + '.en.srt'
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def check_video_file_exists(self, yt):  # 還沒完成
        filepath = yt.video_files_path
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    # def check_trimmed_video_files_exists(self, yt):  # 還沒完成
    #     filepath = yt.trimmed_video_files_path
    #     return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    # def convert_caption_2_txt(self,video_id, video_id_caption):
    #     with open(os.path.join(CAPTIONS_CONVERTED_DIR, video_id + '.txt'), 'w', encoding='utf-8') as f:
    #         for line in video_id_caption:
    #             if line == 'caption':
    #                 continue
    #             f.write(line + ''.rjust(8, ' ') + video_id_caption[line] + '\n')
