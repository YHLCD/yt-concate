from .step import Step
from yt_concate.model.target_captions import TargetCaptions


class Search(Step):
    def process(self, data, inputs, utils):
        search_word = inputs['search_word']
        target_captions = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue
            for caption in captions:
                time = captions[caption]
                if search_word in caption:
                    t = TargetCaptions(yt, caption, time)  # instantiate
                    target_captions.append(t)

        print(len(target_captions))
        return target_captions
