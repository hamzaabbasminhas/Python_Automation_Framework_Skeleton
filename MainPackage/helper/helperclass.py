from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class HelperClass:

    def __init__(self, driver):
        self.driver = driver

    def verifyLinkPresence(self, text, time):
        element = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((By.XPATH, text)))

    def selectOptionByText(self, locator, value):
        sel = Select(locator)
        sel.select_by_value(value)

    def actionChainSendKeys(self, text):
        actions = ActionChains(self.driver)
        actions.send_keys(text)
        actions.perform()

    def rightClickWebElement(self, element):
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    def doubleClickWebElement(self, element):
        action = ActionChains(self.driver)
        action.double_click(element).perform()

    def checkBoxes(self, xpath, option):
        checkboxes = self.driver.find_elements_by_xpath(xpath)

        for checkbox in checkboxes:
            if checkbox.get_attribute("value") == option:
                checkbox.click()
                assert checkbox.is_selected()

    def radioButton(self, indexofRadioButton):
        radioButtons = self.driver.find_elements_by_name("radioButton")
        radioButtons[indexofRadioButton].click()
        assert radioButtons[indexofRadioButton].is_selected()

    def click(self, element):
        element.click()

    def send_keys(self, inputfield, value):
        inputfield.send_keys(value)
