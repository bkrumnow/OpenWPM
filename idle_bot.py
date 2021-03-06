from automation import TaskManager, CommandSequence
import tempfile
import time
import os
import copy
import json
import pdb

NUM_BROWSERS = 1
site = 'http://localhost:8080/deliver.html'

manager_params, browser_params = TaskManager.load_default_params(NUM_BROWSERS)
manager_params['data_directory'] = '~/Desktop/idle/'
manager_params['log_directory'] = '~/Desktop/idle/'
browser_params[0]['cookie_instrument'] = False
browser_params[0]['js_instrument'] = True
browser_params[0]['http_instrument'] = False
browser_params[0]['navigation_instrument'] = False
browser_params[0]['save_all_javascript'] = True

browser_params[0]['headless'] = False  # Launch only browser 0 headless

manager = TaskManager.TaskManager(manager_params, browser_params)

command_sequence = CommandSequence.CommandSequence(site)
command_sequence.get(timeout=100000, sleep=6000)
manager.execute_command_sequence(command_sequence, index='**')
manager.close()