from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))
    
    def send_keys(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def get_error_message(self, by, value):
        return self.find_element(by, value).text

class ContactPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.name_field = (By.ID, "name")
        self.email_field = (By.ID, "email")
        self.message_field = (By.ID, "message")
        self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.name_error = (By.ID, "nameError")
        self.email_error = (By.ID, "emailError")
        self.message_error = (By.ID, "messageError")

    def fill_form(self, name, email, message):
     
        self.send_keys(*self.name_field, name)
        self.send_keys(*self.email_field, email)
        self.send_keys(*self.message_field, message)
    
    def submit_form(self):
        self.click(*self.submit_button)

    def get_name_error(self):
        return self.get_error_message(*self.name_error)

    def get_email_error(self):
        return self.get_error_message(*self.email_error)

    def get_message_error(self):
        return self.get_error_message(*self.message_error)
