from automation import TaskManager, CommandSequence
import csv
import tempfile
import time
import os
import copy
import json
import pdb

NUM_BROWSERS = 8
fileReader = csv.reader(open('./sites/bot_detectors.csv'), delimiter=',')

#NUM_BROWSERS = 2
#fileReader = csv.reader(open('./sites/test.csv'), delimiter=',')

sites = []
for (index, site) in fileReader:
    sites.append(site);
del fileReader
print(sites)

manager_params, browser_params = TaskManager.load_default_params(NUM_BROWSERS)
for i in range(NUM_BROWSERS):
    browser_params[i]['headless'] = True  # Launch only browser 0 headless

manager_params['data_directory'] = '~/Desktop/OpenWPM/data/'
manager_params['log_directory'] = '~/Desktop/OpenWPM/data/'
manager = TaskManager.TaskManager(manager_params, browser_params)    

for site in sites:
    command_sequence = CommandSequence.CommandSequence("http://" + site, True)
    command_sequence.get(sleep=30, timeout=60)
    command_sequence.save_screenshot(site, 5)
    manager.execute_command_sequence(command_sequence, index=None)
    #del command_sequence
manager.close()