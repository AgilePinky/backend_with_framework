import random

import requests.status_codes
from faker import Faker

from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.base_teacher import SubjectEnum

faker = Faker()


class TestChangeTeachersEmailOnExisting:
    def test_change_teachers_subject_on_existing(self, admin_university_api_utils):
        teacher_helper = TeacherHelper(api_utils=admin_university_api_utils)

        first_teacher_subject = random.choice([option for option in SubjectEnum])

        response = teacher_helper.post_teacher({"first_name": faker.first_name(),
                                                "last_name": faker.last_name(),
                                                "subject": first_teacher_subject})

        response = teacher_helper.post_teacher({"first_name": faker.first_name(),
                                                "last_name": faker.last_name(),
                                                "subject": first_teacher_subject})

        assert response.status_code == requests.status_codes.codes.created, \
            (f"Invalid data didn't noticed. Actual status code '{response.status_code}', "
             f"expected '{requests.status_codes.codes.created}'")
