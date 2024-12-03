import os
from constants import *

def play_video(path: str):
	return os.system(f"sudo -u pi cvlc -f --no-video-title-show {path} 2> /dev/null")

def play_boot_video():
	play_video(os.path.join(IDEXCONFIG_PATH, "boot_videos", "default.mp4"))