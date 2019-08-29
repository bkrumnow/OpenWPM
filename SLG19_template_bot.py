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
config = "FX_nightly_68.0_64-bit_headful_mac_os_x_webdriver_v0.24.0"

manager_params, browser_params = TaskManager.load_default_params(NUM_BROWSERS)
manager_params['data_directory'] = './Results/'
manager_params['log_directory'] = './Results/'

browser_params[0]['headless'] = False  # Launch only browser 0 headless
browser_params[0]['stealth_enabled'] = False  # Install stealth extension for webdriver

manager = TaskManager.TaskManager(manager_params, browser_params)

command_sequence = CommandSequence.CommandSequence(site)
command_sequence.get(sleep=5, timeout=60)
command_sequence.execute_template_dialog(config, timeout=60)

manager.execute_command_sequence(command_sequence, index='**')
manager.close()