import os

from pprint import pprint

from .step import Step
from yt_concate.settings import CAPTIONS_SOURCE_DIR
#from yt_concate.settings import CAPTIONS_CONVERTED_DIR


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTIONS_SOURCE_DIR):
            if not caption_file.endswith('.srt'):
                continue
            video_id = caption_file.split('.en.srt')[0]
            video_id_caption = {}  # dictionary # 以video id為名稱的字典，一組time對應到一組caption
            time_line = False
            time = 'time'
            caption = 'caption'
            with open(os.path.join(CAPTIONS_SOURCE_DIR, caption_file), 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line
                        continue
                    if time_line:
                        caption = line
                        video_id_caption[caption] = time
                        time_line = False
            data[video_id] = video_id_caption
            print(video_id, ':', video_id_caption)
            utils.convert_caption_2_txt(video_id, video_id_caption)
        pprint(data)
        return data
