from automation import TaskManager, CommandSequence
import tempfile
import time
import os
import copy
import json
import pdb

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

NUM_BROWSERS = 1

site = 'http://localhost:8080/'
config = "OpenWPM_Intrumentation_Nightly_68.0_Mac_OS_X_headful__geckodriver_v0.24.0"


manager_params, browser_params = TaskManager.load_default_params(NUM_BROWSERS)
manager_params['data_directory'] = './Results/'
manager_params['log_directory'] = './Results/'

INSTRUMENTATION = True
if INSTRUMENTATION:
    manager_params['cookie_instrument'] = True
    manager_params['js_instrument'] = True
    manager_params['http_instrument'] = True
    manager_params['navigation_instrument'] = True
    manager_params['save_content'] = True

browser_params[0]['headless'] = False  # Launch only browser 0 headless
#browser_params[0]['stealth_enabled'] = True  # Install stealth extension for webdriver

manager = TaskManager.TaskManager(manager_params, browser_params)

command_sequence = CommandSequence.CommandSequence(site)
command_sequence.get(sleep=10)
command_sequence.fill_config(config, 5)
command_sequence.take_fingerprint(15)

manager.execute_command_sequence(command_sequence, index='**')
manager.close()