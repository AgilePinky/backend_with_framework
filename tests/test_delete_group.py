from services.university.helpers.group_helper import GroupHelper

from faker import Faker

faker = Faker()


class TestDeleteGroup:
    def test_delete_group(self, admin_auth_api_utils):
        group_helper = GroupHelper(admin_auth_api_utils)

        group_name = faker.name()
        response = group_helper.post_group({"name": group_name})

        group_id = response.json()["id"]
        response = group_helper.
