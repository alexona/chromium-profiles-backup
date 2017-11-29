# Chromium Profiles Backup

## chromium-profiles-backup.py
*This script is making a backup of chromium bookmars and files for each user profile.*

There you should edit the path to chromium folder and path to backup folder.

## chromium-backup.sh
*This bash script executes python backup script*

There you should edit the path to the directory with your backup.py file.

Place this script inside your user directory: /home/*user_name*

## cronetable edit
*Edit your cronetable in order to run backup periodically*

* Open terminal and type $ crontab -e
* Choose the editor (I used Nano)
* Add one line at the bottom that describes how you wish to run the script. For example every hour: 0 * * * * sh chromium-backup.sh
* Save table (in Nano: ctrl+o followed by enter,then ctrl+x to exit after file is saved)
* To show your new table type $ chrontab -l
