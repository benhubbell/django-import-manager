import os

from core.exceptions import (
    InvalidEnvironmentVariableException,
    MissingEnvironmentVariableException,
)
from datetime import datetime

def get_truthy_environment_variable_or_default(key, default):
    environment_variable = os.getenv(key)
    if not environment_variable:
        raise MissingEnvironmentVariableException(f'Missing environment variable: {key}')
    if environment_variable.lower() in ["true", "1"]:
        return True
    if environment_variable.lower() in ["false", "0"]:
        return False
    
    return default

def get_truthy_environment_variable_or_raise(key):
    environment_variable = os.getenv(key)
    if not environment_variable:
        raise MissingEnvironmentVariableException(f'Missing environment variable: {key}')
    if environment_variable.lower() in ["true", "1"]:
        return True
    if environment_variable.lower() in ["false", "0"]:
        return False
    raise InvalidEnvironmentVariableException(f'Invalid environment variable: {key}. Must be True or False')
    

def get_environment_variable_or_raise(key):
    environment_variable = os.getenv(key)
    if not environment_variable:
        raise MissingEnvironmentVariableException(f'Missing environment variable: {key}')
    return environment_variable

# def verify_token(token, salt, hashed_token)