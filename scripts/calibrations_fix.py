import os

def create_symlink_if_not_exists(source_dir, target_dir):
	if not os.path.exists(target_dir):
		try:
			os.symlink(source_dir, target_dir)
		except:
			pass

def fix_calibrations_directory():
	source_directory = "/home/pi/printer_data/config/calibrations"
	target_directory = "/home/pi/printer_data/gcodes/.calibrations"

	create_symlink_if_not_exists(source_directory, target_directory)
