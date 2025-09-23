import os
import yt_dlp

from .step import Step


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        target_caption_set = set([target_caption.yt for target_caption in data])
        print(len(target_caption_set), 'videos to download')
        for yt in target_caption_set:
            video_id = yt.id
            if utils.check_video_file_exists(yt):
                print('found existing video file:', video_id)
                continue
            ydl_opts = {'skip_download': False,
                        'format': 'bestvideo[ext=mp4][height<=1080][fps=60] + bestaudio[ext=m4a] / best[height<=1080] + bestaudio ',
                        'merge_output_format': 'mp4',
                        'outtmpl': yt.video_files_path
                        }
            print('downloading videos:', video_id)
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download(['https://www.youtube.com/watch?v=' + video_id])  # 括號內放入list
            except (KeyError, AttributeError):
                print('Error when downloading', video_id)
                continue
        return data
