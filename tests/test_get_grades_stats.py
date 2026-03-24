import random
from faker import Faker

from logger.logger import Logger
from services.university.models.base_student import DegreeEnum
from services.university.models.base_teacher import SubjectEnum
from services.university.models.grade_request import GradeRequest
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService
from utils.constants import MIN_GRADE, MAX_GRADE

faker = Faker()
expected_quantity_grades = 3


class TestGetGradeStats:
    def test_get_grade_stats(self, admin_university_api_utils):
        Logger.info("### Step 1. Create group")
        university_service = UniversityService(api_utils=admin_university_api_utils)
        group = GroupRequest(name=faker.name())
        group_response = university_service.create_group(group_request=group)
        group_id = group_response.id

        Logger.info("### Step 2. Create student")
        student = StudentRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 email=faker.email(),
                                 degree=random.choice([option for option in DegreeEnum]),
                                 phone=faker.numerify("+7##########"),
                                 group_id=group_response.id)
        student_response = university_service.create_student(student_request=student)
        student_id = student_response.id

        Logger.info("### Step 3. Create teacher")
        teacher = TeacherRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 subject=random.choice([option for option in SubjectEnum]))
        teacher_response = university_service.create_teacher(teacher_request=teacher)
        teacher_id = teacher_response.id

        Logger.info("### Step 4. Create grade")
        for i in range(expected_quantity_grades):
            grade = GradeRequest(teacher_id=teacher_id,
                                 student_id=student_id,
                                 grade=random.randint(MIN_GRADE, MAX_GRADE))
            grade_response = university_service.create_grade(grade_request=grade)

        Logger.info("### Step 5. Show grade statistics")
        grade_response = university_service.get_grade_stats(student_id=94)

        assert grade_response.count == expected_quantity_grades, \
            (f"Grades didn't created as it expected. "
             f"Actual quantity of grades '{grade_response.count}', "
             f"expected quantity of grades 'expected_quantity_grades'")
