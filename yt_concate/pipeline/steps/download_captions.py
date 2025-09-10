import os.path

import yt_dlp

from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.steps.step import StepException

import time


# import的順序：1.bulid in(內建)
#             2.third party(第三方套件)
#             3.自己專案內的檔案。


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start_time = time.time()
        for url in data:
            video_id = utils.get_video_id_from_url(url)
            if utils.check_caption_file_exists(url):
                print('found existing caption file,video_id：', video_id)
                continue
            ydl_opts = {'writesubtitles': True,
                        'writeautomaticsub': True,
                        'skip_download': True,
                        'subtitleslangs': ['en'],
                        'subtitlesformat': 'srt',
                        'outtmpl': utils.get_caption_files_path(url)
                        }
            print('downloading caption file,video_id:', video_id)
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download(['https://www.youtube.com/watch?v=' + video_id])  # 括號內放入list
            except (KeyError, AttributeError):
                print('Error when downloading', video_id)
                continue
        end_time = time.time()
        print(f'took {end_time - start_time} seconds')

    # try:
    #     next_page_token = resp['nextPageToken']
    #     url = first_url + '&pageToken={}'.format(next_page_token)
    # except KeyError:
    #     break
