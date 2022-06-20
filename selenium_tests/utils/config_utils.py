import json
import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, "config.json")
DEFAULT_WAIT_TIME = 10

config_file = open(CONFIG_PATH)
js = json.load(config_file)


def get_project_root_dir():
    return ROOT_DIR


def get_config_json():
    return js


def get_base_url():
    return js["base_url"]


def get_default_time_out():
    return js["timeout"]


def get_user_id():
    return js["user_id"]


def get_user_password():
    return js["user_password"]


def get_browser():
    return js["browser"]