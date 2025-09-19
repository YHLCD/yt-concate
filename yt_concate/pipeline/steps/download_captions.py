import yt_dlp

from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.steps.step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            video_id = yt.id
            url = yt.url
            if utils.check_caption_file_exists(yt):
                print('found existing caption file:', video_id)
                continue
            ydl_opts = {'writesubtitles': True,
                        'writeautomaticsub': True,
                        'skip_download': True,
                        'subtitleslangs': ['en'],
                        'subtitlesformat': 'srt',
                        'outtmpl': yt.caption_files_path
                        }
            print('downloading caption file,video_id:', video_id)
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download(['https://www.youtube.com/watch?v=' + video_id])  # 括號內放入list
            except (KeyError, AttributeError):
                print('Error when downloading', url)
                continue
        return data
