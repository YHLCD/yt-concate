from .step import Step


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if not utils.check_caption_file_exists(yt):
                continue
            video_id_caption = {}
            with open(yt.caption_files_path + '.en.srt', 'r', encoding='utf-8') as f:
                time_line = False
                time = 'time'
                caption = 'caption'
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
            yt.captions = video_id_caption
            print(yt.id, ':', yt.captions)
            # utils.convert_caption_2_txt(yt.id, yt.captions)

        return data
