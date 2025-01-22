import subprocess

def fix_gcodes_permissions():
	try:
		subprocess.run("sudo chown pi /home/pi/printer_data/gcodes")
		subprocess.run("sudo chown pi /home/pi/printer_data/gcodes/.JOB")
	except:
		pass