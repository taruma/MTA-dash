"""This module reads the configuration file and converts it to a namespace."""

import tomllib
from types import SimpleNamespace

def dict_to_namespace(d):
    """Convert a dictionary to a namespace."""
    for key, value in d.items():
        if isinstance(value, dict):
            d[key] = dict_to_namespace(value)
    return SimpleNamespace(**d)

with open('config.toml', 'rb') as f:
    config_dict = tomllib.load(f)

appconfig = dict_to_namespace(config_dict)