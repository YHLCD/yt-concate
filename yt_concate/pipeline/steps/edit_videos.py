import os

from moviepy import VideoFileClip, concatenate_videoclips

from .step import Step


class EditVideos(Step):
    def process(self, data, inputs, utils):
        clips = []
        output_file_path = utils.get_output_file_path(channel_id=inputs['channel_id'],
                                                      search_word=inputs['search_word'])
        if os.path.exists(output_file_path) and os.path.getsize(output_file_path) > 0:
            print('Video already processed')
        else:
            print('Processing video')
            for target_caption in data:
                # 註解部分是生成影片片段，並且放入特定資料夾，但這個程式主要是要取得最後的合併影片檔，影片片段檔沒留的必要，因此先不使用這功能。
                # filename = target_caption.yt.id + self.parse_time_in_name(target_caption) + '.mp4'
                # filepath = os.path.join(target_caption.yt.trimmed_videos_dir, filename)

                start_time, end_time = target_caption.time.split(' --> ')
                clip = VideoFileClip(target_caption.yt.video_files_path).subclipped(start_time, end_time)
                clips.append(clip)
                if len(clips) >= inputs['limit']:
                    break

                # if os.path.exists(filepath) and os.path.getsize(filepath) > 0:  # 檢查trimmed vidoe是否存在。
                #     print('found existing trimmed video file:', filename)
                # else:
                #     target_caption.yt.create_trimmed_videos_dir()
                #     clip.write_videofile(filepath)
            output = concatenate_videoclips(clips, method='chain')
            output.write_videofile(output_file_path)

    def parse_time_in_name(self, target_caption):
        time_in_name = target_caption.time.split(' --> ')[0].replace(',', '').replace(':', '') + \
                       target_caption.time.split(' --> ')[1].replace(',', '').replace(':', '')
        return time_in_name
