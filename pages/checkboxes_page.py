from Locators.locators import CheckBoxesLocators
from pages.base_page import BasePage


class CheckBoxes(BasePage):

    def should_be_checkbox1_unchecked(self):
        checkbox1 = self.browser.find_element(*CheckBoxesLocators.CHECKBOX1)
        checkbox1_checked = checkbox1.get_attribute("checked")
        assert checkbox1_checked is None, "Checkbox1 is selected!"

    def tick_checkbox1(self):
        checkbox1 = self.browser.find_element(*CheckBoxesLocators.CHECKBOX1)
        checkbox1.click()

    def should_be_checkbox1_checked(self):
        checkbox1 = self.browser.find_element(*CheckBoxesLocators.CHECKBOX1)
        checkbox1_checked = checkbox1.get_attribute("checked")
        assert checkbox1_checked is not None, "Checkbox1 is not selected!"