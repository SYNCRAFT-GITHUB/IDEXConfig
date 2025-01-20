from transfer import update_printer_config
from boot_video import play_boot_video
from variables_fix import fix_variables_file
from calibrations_fix import fix_calibrations_directory

update_printer_config()
fix_variables_file()
fix_calibrations_directory()
play_boot_video()