from automation import TaskManager, CommandSequence
import csv
import tempfile
import time
import os
import copy
import json
import pdb

#NUM_BROWSERS = 8
#fileReader = csv.reader(open('./sites/bot_detectors.csv'), delimiter=',')

NUM_BROWSERS = 1
fileReader = csv.reader(open('./sites/test_set.csv'), delimiter=',')
sites = []
for (index, site) in fileReader:
    sites.append(site);
del fileReader
print(sites)

manager_params, browser_params = TaskManager.load_default_params(NUM_BROWSERS)
for i in range(NUM_BROWSERS):
    browser_params[i]['headless'] = False  # Launch only browser 0 headless
    browser_params[i]['stealth_enabled'] = False # Avoid to load stealh extension
    browser_params[i]['js_instrument'] = True
    browser_params[i]['save_all_content'] = True
    #browser_params[i]['save_javascript'] = True
        
manager_params['data_directory'] = './Results/'
manager_params['log_directory'] = './Results/'
manager = TaskManager.TaskManager(manager_params, browser_params)    

for i, site in enumerate(sites):
    command_sequence = CommandSequence.CommandSequence("http://" + site, True)
    command_sequence.get(sleep=20, timeout=60)
    command_sequence.save_screenshot(site, 5)
    manager.dump_profile(os.path.expanduser('./Results/dump'), close_webdriver=True)
    manager.execute_command_sequence(command_sequence, index=None)
    #del command_sequence
manager.close()
