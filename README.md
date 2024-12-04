# Syncraft IDEX

Main repository for the Syncraft IDEX 3D printer.

Should be cloned named as `config` in the `printer_data` repository.

## Files

### Required

#### `canbus_uuids.json`

Should have two properties with string values: `mcu` and `mcu rp2040`.

## Directories

### `/.theme`

Custom images and css used on Mainsail.

### `/backups`

Files that will be on .gitignore, but need to be updated.

### `/boot_videos`

Startup videos.

### `/build`

Instructions and scripts required for building the machine for the first time. 

### `/scripts`

Python scripts used on startup.