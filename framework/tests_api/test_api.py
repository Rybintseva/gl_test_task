from framework.api_client.methods_api import ApiClient
from framework.common.utils import generate_random_string, is_dict_in_dict
from framework.core.settings import SOURCE_USERS_URL, NOT_FOUND


class TestAPI:
    user_id = None
    api_page = ApiClient()

    def test_create_user(self, user_data):
        user_data['name'] = f'Test_{generate_random_string(5)}'
        user_data['email'] = f'Test@{generate_random_string(5)}.{generate_random_string(3)}'
        TestAPI.user_id = self.api_page.create_user(SOURCE_USERS_URL, data=user_data)
        response_user_data = self.api_page.get_user_data(SOURCE_USERS_URL, self.user_id)
        assert is_dict_in_dict(response_user_data['data'], user_data), \
            f'User was not created. Actual user data: {response_user_data["data"]}. Expected: {user_data}'

    def test_modify_user(self, user_data):
        user_data['name'] = f"Mod_{user_data['name']}"
        user_data['email'] = f"Mod_{user_data['email']}"
        self.api_page.modify_user(SOURCE_USERS_URL, self.user_id, data=user_data)
        response_user_data = self.api_page.get_user_data(SOURCE_USERS_URL, self.user_id)
        assert is_dict_in_dict(response_user_data['data'], user_data), \
            f'User was not modified. Actual user data: {response_user_data["data"]}. Expected: {user_data}'

    def test_remove_user(self, user_data):
        self.api_page.remove_user(SOURCE_USERS_URL, self.user_id, data=user_data)
        response = self.api_page.get_user_data(SOURCE_USERS_URL, self.user_id)['code']
        assert response == NOT_FOUND, \
            f'User was not removed. Actual status code: {response} Expected: {NOT_FOUND}'
