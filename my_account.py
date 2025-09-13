from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

print "my_account.py"

class MyAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://test.zervant.com"
        self.verificationErrors = []
    
    def test_my_account(self):
        driver = self.driver
        driver.get("http://test.zervant.com/login/#en")
        driver.maximize_window()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("dasko@zervant.com")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("dasko@zervant.com")
        driver.find_element_by_id("submitbutton").click()
        self.assertEqual("Zervant", driver.title)
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "mainNavigation-travel"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr/td/div/h3/a").click()
        # ERROR: Caught exception [ERROR: Unsupported command [setSpeed | 2000 | ]]
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*logo[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr/td/div[2]/div[12]/div[10]/div[2]/div/div[2]/div/div[2]/div[2]/div/div").click()
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*Invoicing language[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr/td/div[2]/div[12]/div[10]/div[2]/div/div[2]/div/div[2]/div[3]/div/div").click()
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*Send e-mail reminders[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr/td/div[2]/div[12]/div[10]/div[2]/div/div[2]/div/div[2]/div[4]/div/div").click()
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*A Daskalopoulos[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr/td/div[2]/div[12]/div[10]/div[2]/div/div[2]/div/div[2]/div[5]/div/div").click()
        try: self.assertTrue(self.is_element_present(By.ID, "importProducts"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr/td/div[2]/div[12]/div[10]/div/div/div[2]/div/div[2]/div[6]/div/div").click()
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*Teemu[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr/td/div[2]/div[12]/div[10]/div/div/div[2]/div/div[2]/div[7]/div/div").click()
        try: self.assertTrue(self.is_element_present(By.ID, "account-webpage-edit"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr/td/div[2]/div[12]/div[10]/div/div/div[2]/div/div[2]/div[8]/div/div").click()
        try: self.assertTrue(self.is_element_present(By.ID, "addFinancialYearLink"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr/td/div[2]/div[12]/div[10]/div/div/div[2]/div/div[2]/div[9]/div/div").click()
        try: self.assertTrue(self.is_element_present(By.ID, "subscriptionTEAM-save"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "subscription-invite"))
        except AssertionError as e: self.verificationErrors.append(str(e))
    
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
