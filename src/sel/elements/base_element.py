from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from util.driver_container import DriverContainer


class BaseElement:
    timeout = 20
    driver: WebDriver

    def __init__(self, selector):
        self.selector = selector
        self.driver = DriverContainer().get_driver(DriverContainer)
        return

    def wait_until_clickable(self) -> WebElement:
        element = WebDriverWait(self.driver, self.timeout,
                                ignored_exceptions=(ElementClickInterceptedException,
                                                    StaleElementReferenceException)).until(
            EC.element_to_be_clickable(self.selector))
        return element

    def wait_until_visible(self) -> WebElement:
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.selector))
        return element

    def wait_until_present(self) -> WebElement:
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.selector))
        return element

    def wait_until_not_visible(self) -> WebElement:
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.invisibility_of_element(self.selector))
        return element

    def wait_until(self) -> WebElement:
        element = WebDriverWait(self.driver, self.timeout, ignored_exceptions=ElementClickInterceptedException).until(
            EC.element_to_be_clickable(self.selector))
        return element