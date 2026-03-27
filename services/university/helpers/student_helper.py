import requests

from services.general.helpers.base_helper import BaseHelper

class StudentHelper(BaseHelper):
    ENDPOINT_PREFIX = "/students"

    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"

    def post_student(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def get_current_student(self, item) -> requests.Response:
        response = self.api_utils.get_with_id(self.ROOT_ENDPOINT, item)
        return response

    def put_student(self, item, data: dict) -> requests.Response:
        response = self.api_utils.put(self.ROOT_ENDPOINT, item, data=data)
        return response