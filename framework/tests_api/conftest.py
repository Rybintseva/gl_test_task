import json
import os

import pytest

from framework.core import config


@pytest.fixture(scope='session')
def user_data():
    with open(os.path.join(config.HOME_PATH, 'data', 'user_data.json'),
              encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data
