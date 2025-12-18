import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert  
from ContactPage import ContactPage  

class TestContactForm(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())  
        self.driver = webdriver.Chrome(service=service)  
        self.driver.get("file:///E:/Lab4/web.html")  

    def tearDown(self):
        self.driver.quit()

    def close_alert_if_present(self):
        try:
            alert = Alert(self.driver)
            alert.accept()  
        except:
            pass  

    def test_invalid_name(self):
        contact_page = ContactPage(self.driver)
        contact_page.fill_form("", "doducdung1701@gmail.com", "This is a message.")
        contact_page.submit_form()
        self.close_alert_if_present()  
        self.assertNotEqual(contact_page.get_name_error(), "")
        print("Test invalid name passed.")
if __name__ == "__main__":
    unittest.main()
