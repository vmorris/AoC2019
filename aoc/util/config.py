import configparser
import os
from pathlib import Path


APP_NAME = 'AoC2019'
APP_HOME = os.path.join(str(Path.home()), f'git/github.com/vmorris/{APP_NAME}')
CONFIG_FILE = os.path.join(APP_HOME, 'config.ini')


class Config:
    def __init__(self):
        if not os.path.exists(CONFIG_FILE):
            self._create_new_config()

    def read_config(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        return config

    def _create_new_config(self):
        config = configparser.ConfigParser()
        if not os.path.exists(APP_HOME):
            os.makedirs(APP_HOME)
        config = configparser.ConfigParser()
        config['DEFAULT'] = {
            'debug': False,
            'app_home': APP_HOME,
            'data_dir': os.path.join(APP_HOME, 'data')
        }
        with open(CONFIG_FILE, 'w') as configfile:
            config.write(configfile)
