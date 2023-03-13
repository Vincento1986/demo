from methods import CheckBoxes
from Content.content import CheckboxContent


def test_checkbox1(browser):
    page = CheckBoxes(browser, CheckboxContent.link)
    page.open()
    page.should_be_checkbox1_unchecked()
    page.tick_checkbox1()
    page.should_be_checkbox1_checked()
