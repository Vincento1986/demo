from pages.status_code_page import StatusCode
from Content.content import StatusCodeContent


def test_check_status_200(browser):
    page = StatusCode(browser, StatusCodeContent.link200)
    page.check_status_200(StatusCodeContent.link200)


def test_check_status_500(browser):  # этот тест должен упасть
    page = StatusCode(browser, StatusCodeContent.link500)
    page.check_status_200(StatusCodeContent.link500)
