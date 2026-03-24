import requests

from services.general.helpers.base_helper import BaseHelper


class GradeHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades"
    STATS_ENDPOINT_PREFIX = "stats"

    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"
    STATS_ENDPOINT = ROOT_ENDPOINT + f"{STATS_ENDPOINT_PREFIX}/"

    def post_grade(self, data: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, data=data)
        return response

    def get_grade_stats(self, params) -> requests.Response:
        response = self.api_utils.get_with_query(
            self.STATS_ENDPOINT, queries=params)
        return response