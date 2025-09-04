from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.step import StepException

from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCVbq2Gz2FNcGUnB7Y6efS9w'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
    }

    steps = [
         GetVideoList(),  #class
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
