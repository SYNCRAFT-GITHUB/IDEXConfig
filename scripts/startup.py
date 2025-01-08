import os
import shutil
from transfer import update_printer_config
from boot_video import play_boot_video
from constants import *

update_printer_config()

if not os.path.exists(VARIABLES_PATH):
	shutil.copyfile(BACKUP_VARIABLES_PATH, VARIABLES_PATH)	

play_boot_video()