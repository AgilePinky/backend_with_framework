import random
from faker import Faker

from services.auth.helpers.auth_helper import AuthHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.auth.helpers.user_helper import UserHelper
from utils.api_utils import ApiUtils

AUTH_URL = "http://localhost:8000"
UNIVERSITY_URL = "http://localhost:8001"

REGISTER_ENDPOINT = "/auth/register/"
LOGIN_ENDPOINT = "/auth/login/"
ME_ENDPOINT = "/users/me/"
GROUPS_ENDPOINT = "/groups/"
STUDENTS_ENDPOINT = "/students/"

faker = Faker()

username = faker.user_name()
password = faker.word() + "!fgsd1"
authorization_helper = AuthHelper(api_utils=ApiUtils(AUTH_URL))

response = authorization_helper.post_register(
    data={"username": username,
          "password": password,
          "password_repeat": password,
          "email": faker.email()})

response = authorization_helper.post_login(
    data={"username": username,
          "password": password})

access_token = response.json()["access_token"]

admin_auth_api_utils = ApiUtils(AUTH_URL,
                                   headers={"Authorization": f"Bearer {access_token}"})
admin_user_helper = UserHelper(admin_auth_api_utils)

admin_university_api_utils = ApiUtils(UNIVERSITY_URL,
                                           headers={"Authorization": f"Bearer {access_token}"})
admin_group_helper = GroupHelper(admin_university_api_utils)
admin_student_helper = StudentHelper(admin_university_api_utils)

response = admin_user_helper.get_me()
response = admin_group_helper.post_group(
    json={"name": faker.name()})
response = admin_student_helper.post_student(
    json={"first_name": faker.first_name(),
          "last_name": faker.last_name(),
          "email": faker.email(),
          "degree": random.choice(["Associate",
                                   "Bachelor",
                                   "Master",
                                   "Doctorate"]),
          "phone": faker.numerify("+7##########"),
          "group_id": response.json()["id"]})
