from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class UrbanRoutesPage:

# Seccao DE e PARA
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
             self.driver = driver
             self.wait = WebDriverWait(driver, 10)


    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

         # Endereco

    def _get_text(self, locator, text):
        return self._find(locator)

    def get_value(self, locator):
        return self.find(locator).get_attribute('value')

    def enter_locations(self, from_text, to_text):
        self.type(self.from_field, from_text)
        self.type(self.to_field, to_text)

    def get_from_location(self):
        return self.get_value(self.from_field)

    def get_to_location(self):
        return self.get_value(self.to_field)







