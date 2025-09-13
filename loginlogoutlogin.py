from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

print "\nloginlogoutlogin.py"

class Loginlogoutlogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.2.8/"
        self.verificationErrors = []
    
    def test_loginlogoutlogin(self):
        driver = self.driver
        driver.get("http://192.168.2.8/login/")
	driver.maximize_window()	
        self.assertEqual("Zervant", driver.title)
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("dasko@zervant.com")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("dasko@zervant.com")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("dasko@zervant.com")
        driver.find_element_by_id("submitbutton").click()
        for i in range(60):
            try:
                if "Zervant - Invoicing, time tracking, and bookkeeping online" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.assertEqual("Zervant - Invoicing, time tracking, and bookkeeping online", driver.title)
        driver.get("http://192.168.2.8/login/")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("dasko@zervant.com")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("dasko@zervant.com")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("dasko@zervant.com")
        driver.find_element_by_id("submitbutton").click()
        # Warning: waitForTextPresent may require manual changes
        for i in range(60):
            try:
                if re.search(r"^[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            except: pass
            time.sleep(3)
        else: self.fail("time out")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
  unittest.main()
