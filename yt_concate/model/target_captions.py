class TargetCaptions(object):
    def __init__(self, yt, caption, time):
        self.yt = yt
        self.caption = caption
        self.time = time

    def __str__(self):
        return '<TargetCaptions(yt=' + str(self.yt) + ')>'

    def __repr__(self):
        content = ' ♥ '.join([
            'yt=' + str(self.yt),
            'caption=' + str(self.caption),
            'time=' + str(self.time)
        ])
        return '<TargetCaptions(' + content + ')>'
        # 上面的♥可以替換成自己想要的東西來做分隔
