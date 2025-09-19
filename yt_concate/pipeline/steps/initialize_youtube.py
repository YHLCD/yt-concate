from .step import Step
from yt_concate.model.youtube import Youtube


class InitializeYoutube(Step):
    def process(self, data, inputs, utils):
        return [Youtube(url) for url in data]
