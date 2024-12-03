# Building a machine

1. Install softwares with KIAUH
	- Klipper
	- Moonraker
	- Mainsail
	- Crowsnest
	- SwierVision
2. Run `apply.sh`
3. Run `python3 /home/pi/katapult/scripts/flashtool.py -i can0 -q`
4. Add a file `../canbus_uuids.json` with the two values outputted by the former command: `mcu` and `mcu rp2040`