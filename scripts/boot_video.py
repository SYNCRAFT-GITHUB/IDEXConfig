import os
import subprocess
from constants import *

def play_video(path: str):
	return subprocess.run(["sudo", "-u", "pi", "cvlc", "-f", "--no-video-title-show", path])

def play_boot_video():
	play_video(os.path.join(IDEXCONFIG_PATH, "boot_videos", "default.mp4"))