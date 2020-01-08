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

site = 'http://localhost:8080/biometry.html'

manager_params, browser_params = TaskManager.load_default_params(NUM_BROWSERS)
manager_params['data_directory'] = './Results/'
manager_params['log_directory'] = './Results/'

INSTRUMENTATION = False
if INSTRUMENTATION:
    browser_params['cookie_instrument'] = False
    browser_params['js_instrument'] = False
    browser_params['http_instrument'] = False
    browser_params['navigation_instrument'] = False
    browser_params['save_content'] = False

browser_params[0]['headless'] = False  # Launch only browser 0 headless
#browser_params[0]['stealth_enabled'] = True  # Install stealth extension for webdriver

manager = TaskManager.TaskManager(manager_params, browser_params)

command_sequence = CommandSequence.CommandSequence(site)
command_sequence.get(sleep=3)
command_sequence.perform_behavioural_biometric_test()

manager.execute_command_sequence(command_sequence, index='**')
manager.close()