"""
Install template attack server from: https://github.com/IAIK/jstemplate

"""

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
config = "OpenWPM_Nightly_68.0_Mac_OS_X_headful__geckodriver_v0.24.0"

manager_params, browser_params = TaskManager.load_default_params(NUM_BROWSERS)
manager_params['data_directory'] = './Results/'
manager_params['log_directory'] = './Results/'

#Setting up full instrumentation
INSTRUMENTATION = False
if INSTRUMENTATION:
    manager_params['cookie_instrument'] = True
    manager_params['js_instrument'] = True
    manager_params['http_instrument'] = True
    manager_params['navigation_instrument'] = True
    manager_params['save_content'] = True

#    "js_instrument_modules": "fingerprinting",

browser_params[0]['headless'] = False  # Launch only browser 0 headless. Note: Always True under MacOS X
browser_params[0]['stealth_enabled'] = False  # Install stealth extension for webdriver

manager = TaskManager.TaskManager(manager_params, browser_params)

command_sequence = CommandSequence.CommandSequence(site)
command_sequence.get(sleep=5, timeout=60)
command_sequence.execute_template_dialog(config, timeout=60)

manager.execute_command_sequence(command_sequence, index='**')
manager.close()