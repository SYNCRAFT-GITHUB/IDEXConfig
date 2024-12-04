import os

HOME = os.path.join("/home", "pi")

IDEXCONFIG_PATH = os.path.join(HOME, "printer_data", "config")
PRINTER_CFG_PATH = os.path.join(HOME, "printer_data", "config", "printer.cfg")

BACKUP_PRINTER_CFG_PATH = os.path.join(IDEXCONFIG_PATH, "backups", "printer.cfg")
CANBUS_UUIDS_PATH = os.path.join(IDEXCONFIG_PATH, "canbus_uuids.json")