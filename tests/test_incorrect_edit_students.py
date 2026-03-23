import random

import requests.status_codes
from faker import Faker

from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper

from services.university.models.base_student import DegreeEnum

faker = Faker()


class TestIncorrectEditStudent:
    def test_incorrect_edit_student(self, admin_university_api_utils):
        group_helper = GroupHelper(api_utils=admin_university_api_utils)

        group_helper = group_helper.post_group({"name": faker.name()})
        group_id = group_helper.json()["id"]

        student_helper = StudentHelper(api_utils=admin_university_api_utils)

        response = student_helper.post_student({"first_name": faker.first_name(),
                                                "last_name": faker.last_name(),
                                                "email": faker.email(),
                                                "degree": random.choice([option for option in DegreeEnum]),
                                                "phone": faker.numerify("+7##########"),
                                                "group_id": group_id})

        student_id = response.json()["id"]

        response = student_helper.put_student(student_id,
                                              {"first_name": faker.first_name(),
                                               "last_name": faker.last_name(),
                                               "email": faker.numerify("+7##########"),
                                               "degree": random.choice([option for option in DegreeEnum]),
                                               "phone": faker.numerify("+7##########"),
                                               "group_id": group_id})

        assert response.status_code == requests.status_codes.codes.unprocessable_content,\
            (f"Invalid data didn't noticed. Actual status code '{response.status_code}', "
             f"expected '{requests.status_codes.codes.unprocessable_content}'")