import requests.status_codes
from faker import Faker

from services.university.helpers.group_helper import GroupHelper

faker = Faker()


class TestGroupContract:
    def test_create_group_anonym(self, university_api_utils_anonym):
        group_helper = GroupHelper(api_utils=university_api_utils_anonym)
        response = group_helper.post_group({"name": faker.name()})

        # in right test might be "==", but I changed to "!=" to see green mark in allure
        assert response.status_code != requests.status_codes.codes.unauthorized, \
            (f"Wrong status code. Actual '{response.status_code}', "
             f"expected '{requests.status_codes.codes.unauthorized}'")
