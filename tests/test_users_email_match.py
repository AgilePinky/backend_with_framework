import requests.status_codes

from services.auth.helpers.auth_helper import AuthHelper
from services.auth.helpers.user_helper import UserHelper
from faker import Faker

faker = Faker()


class TestUsersEmailMatch:
    def test_users_email_match(self, auth_api_utils_anonym, admin_auth_api_utils):
        auth_helper = AuthHelper(api_utils=auth_api_utils_anonym)
        user_helper = UserHelper(api_utils=admin_auth_api_utils)

        response = user_helper.get_me()
        current_username = response.json()["username"]
        password = faker.password(length=30,
                                  digits=True,
                                  upper_case=True,
                                  lower_case=True,
                                  special_chars=True)

        response = auth_helper.post_register({"username": current_username,
                                              "password": password,
                                              "password_repeat": password,
                                              "email": faker.email()})

        assert response.status_code == requests.status_codes.codes.conflict, \
            (f"Conflict with existing data. Actual status code '{response.status_code}', "
             f"expected '{requests.status_codes.codes.conflict}'")

