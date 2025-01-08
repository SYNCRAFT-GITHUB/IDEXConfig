import os
import shutil
import configparser
from constants import *

def fix_variables_file():
	machine_found = False

	if os.path.exists(VARIABLES_PATH):
		variables = configparser.ConfigParser()
		variables.read(VARIABLES_PATH)
		if "Variables" in variables:
			machine_found = "machine" in variables["Variables"]

	if not machine_found:
		shutil.copyfile(BACKUP_VARIABLES_PATH, VARIABLES_PATH)

	# Own it either way
	shutil.chown(VARIABLES_PATH, "pi")
	