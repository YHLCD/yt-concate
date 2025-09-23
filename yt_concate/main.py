import time

from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_youtube import InitializeYoutube
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.edit_videos import EditVideos
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils
from yt_concate.settings import CHANNEL_ID


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'coffee',
        'limit': 20,
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYoutube(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideos(),
        Postflight(),
    ]

    start = time.time()

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)

    end = time.time()
    print('Total time:', end - start)


if __name__ == '__main__':
    main()
