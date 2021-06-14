from requests import Session

from framework.core.logger import LOGGER
from framework.core.settings import HEADERS


class ApiClient:
    def __init__(self):
        self.session = Session()

    def create_user(self, url, **kwargs):
        LOGGER.info('Creating new user')
        response = self.session.post(url, **kwargs, headers=HEADERS)
        user_id = response.json()['data']['id']
        return user_id

    def get_user_data(self, url, user_id):
        LOGGER.info('Getting the user data')
        user_data = self.session.get(f'{url}/{user_id}').json()
        return user_data

    def modify_user(self, url, user_id, **kwargs):
        LOGGER.info('Modifying the user')
        return self.session.patch(f'{url}/{user_id}', **kwargs, headers=HEADERS)

    def remove_user(self, url, user_id, **kwargs):
        LOGGER.info('Removing the user')
        return self.session.delete(f'{url}/{user_id}', **kwargs, headers=HEADERS)
