import os
import configparser
import json
from constants import *

if not os.path.exists(PRINTER_CFG_PATH):
	raise FileNotFoundError("printer.cfg not found")

if not os.path.exists(CANBUS_UUIDS_PATH):
	raise FileNotFoundError("canbus_uuids.json not found")

def extract_save_config():
	SAVE_CONFIG_LINE = "#*# <---------------------- SAVE_CONFIG ---------------------->"

	save_config = []
	found_save_config_line = False

	with open(PRINTER_CFG_PATH, 'r') as printer_cfg:
		for line in printer_cfg:
			if SAVE_CONFIG_LINE in line:
				found_save_config_line = True
			if found_save_config_line:
				save_config.append(line)

	return save_config

def get_canbus_uuids():
	with open(CANBUS_UUIDS_PATH, 'r') as canbus_uuids:
		data: dict = json.load(canbus_uuids)

		mcu_uuid: str = data.get("mcu")
		mcu_rp2040_uuid: str = data.get("mcu rp2040")

		return mcu_uuid, mcu_rp2040_uuid

def replace_canbus_uuids(mcu_uuid, rp2040_uuid):
	replaced_backup_printer_cfg = configparser.ConfigParser()
	replaced_backup_printer_cfg.read(BACKUP_PRINTER_CFG_PATH)

	if "mcu" in replaced_backup_printer_cfg:
		replaced_backup_printer_cfg["mcu"]["canbus_uuid"] = mcu_uuid
	if "mcu rp2040" in replaced_backup_printer_cfg:
		replaced_backup_printer_cfg["mcu rp2040"]["canbus_uuid"] = rp2040_uuid

	return replaced_backup_printer_cfg

def update_printer_config():
	save_config = extract_save_config()
	mcu_uuid, mcu_rp2040_uuid = get_canbus_uuids()
	replaced_backup_printer_cfg = replace_canbus_uuids(mcu_uuid, mcu_rp2040_uuid)

	with open(PRINTER_CFG_PATH, 'w') as printer_cfg:
		replaced_backup_printer_cfg.write(printer_cfg)
		printer_cfg.writelines(save_config)