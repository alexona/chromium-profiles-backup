#! /usr/bin/python3
"""
chromium-profiles-backup.py:
This script is making a backup of chromium bookmars and files for each user profile.
"""

__author__ = 'Monika Kubek'
__email__ = 'kubek.monika@wp.pl'


import shutil
import os
import sys
import re
import time


# path to chromium directory
# usually in /home/user/.config/
pathToChromium = '/home/monika/.config/chromium/'
# path to folder where you would like to store your backup
pathToBackupFolder = '/home/monika/HDD/Backup/chromium-profiles/'
# name of files you would like to backup
filesToBackup = ('Bookmarks', 'Bookmarks.bak', 'Current Session', 'Current Tabs')

# list of all profiles
profiles = [x for x in os.listdir(pathToChromium) if re.search('^Profile', x)]
profiles.sort()

def write_to_log(message, newlines=1):
    """
    Write a message followed by a given number of newlines
    into a log file in backup folder.
    """
    global pathToBackupFolder
    logFile = pathToBackupFolder + 'backup.log'
    with open(logFile, mode='a') as log:
        log.write(message + '\n'*newlines)

if __name__ == '__main__':
    # write current time
    write_to_log('#' * 20 + '\n' + ' '.join([str(x) for x in time.gmtime(time.time())]), 2)

    for profile in profiles:
        write_to_log('--- {} ---'.format(profile))
        sourceDir = pathToChromium + profile  # path to source directory
        targetDir = pathToBackupFolder + profile  # path to target directory

        try:  # try to make a backup directory for a profile if it does not exists
            os.mkdir(targetDir)
            write_to_log('\tCreate directory <{}> in backup path'.format(profile))
        except FileExistsError:
            write_to_log('\tDirectory <{}> in backup path already exist'.format(profile))
        except:
            write_to_log('\tUnexpected error while creating directory: {}'.format(sys.exc_info()))
            sys.exit(1)

        write_to_log('\t..Making copy...')

        for aFile in filesToBackup: 
            write_to_log('\t-> file <{}>:  '.format(aFile))
            try:
                shutil.copyfile(sourceDir + '/' + aFile, targetDir + '/' + aFile)
            except:
                write_to_log('\t\tUnexpected error while making copy: {}'.format(sys.exc_info()))
            else:
                write_to_log('\t\tSuccess!')

    write_to_log('DONE!', 3)
