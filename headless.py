from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# For headless tests
options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome()  # Comment out this line for headless execution & uncomment the line below
# driver = webdriver.Chrome(options=options, executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.get('http://www.python.org')
assert 'Python' in driver.title
elem = driver.find_element_by_name('q')
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
