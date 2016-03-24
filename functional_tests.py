from selenium import webdriver

the_host = "http://localhost:8000"

driver = webdriver.Firefox()
driver.get(the_host)
assert "Django" in driver.title
driver.close()
