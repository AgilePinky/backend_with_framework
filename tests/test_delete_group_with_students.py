import random

import requests

from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from faker import Faker

from services.university.models.base_student import DegreeEnum

faker = Faker()


class TestDeleteGroupWithStudents:
    def test_delete_group_with_students(self, admin_university_api_utils):
        group_helper = GroupHelper(api_utils=admin_university_api_utils)

        response = group_helper.post_group({"name": faker.name()})

        group_id = response.json()["id"]
        student_helper = StudentHelper(api_utils=admin_university_api_utils)

        response = student_helper.post_student({"first_name": faker.first_name(),
                                                "last_name": faker.last_name(),
                                                "email": faker.email(),
                                                "degree": random.choice([option for option in DegreeEnum]),
                                                "phone": faker.numerify("+7##########"),
                                                "group_id": group_id})

        student_id = response.json()["id"]
        response = group_helper.delete(group_id)

        assert response.status_code == requests.status_codes.codes.ok, \
            (f"Problem with deleting. Actual status code '{response.status_code}', "
             f"expected '{requests.status_codes.codes.ok}'")

        response = student_helper.get_current_student(student_id)

        assert response.status_code == requests.status_codes.codes.not_found, \
            (f"Student still exist. Actual status code '{response.status_code}', "
             f"expected '{requests.status_codes.codes.not_found}'")
