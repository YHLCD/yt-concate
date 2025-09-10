import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

CHANNEL_ID = 'UCZJiDye9aqg68BfMNbFS5jw'

DOWNLOADS_DIR = 'downloads'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
VIDEOS_SOURCE_DIR = os.path.join(VIDEOS_DIR, CHANNEL_ID)
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')
CAPTIONS_SOURCE_DIR = os.path.join(CAPTIONS_DIR, CHANNEL_ID)
VIDEOS_LIST_DIR = os.path.join(DOWNLOADS_DIR, 'videos_list')  # video_list 資料夾的路徑
