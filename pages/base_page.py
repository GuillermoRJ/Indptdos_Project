from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # Espera dinámica para elementos renderizados en Angular
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, *locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, *locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()