import requests

from pages.base_page import BasePage


class StatusCode(BasePage):

    def check_status_200(self, link):
        response = requests.get(link)
        assert response.status_code == 200, f"status code = {response.status_code}"