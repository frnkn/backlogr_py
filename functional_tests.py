from selenium import webdriver
import unittest
"""
the_host = "http://localhost:8000"

driver = webdriver.Firefox()
driver.get(the_host)
assert "Django" in driver.title
driver.close()
"""
class BacklogIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.the_host = "http://localhost:8000"

    def tearDown(self):
        self.driver.close()

    def test_start_page(self):
        #User navigates to the start page
        self.driver.get(self.the_host + "/")

        #He mentions the start page content as it has the class ta-start-page-jumbo
        self.assertTrue(self.driver.find_element_by_class_name('ta-start-page-jumbo'))

    def test_meta_pages(self):
        #User navigates to the imprint page
        self.driver.get(self.the_host + "/imprint")

        #He sees the imprint page
        self.assertTrue(self.driver.find_element_by_class_name('ta-imprint'))

        #He goes to the legal page
        self.driver.get(self.the_host + "/legal")

        #He sees the legal page
        self.assertTrue(self.driver.find_element_by_class_name('ta-legal'))


    def test_login_and_backlog_mgmt(self):
        #User navigates to login to get the login mask
        self.driver.get(self.the_host + "/login")

        #User sees the login form
        self.assertTrue(self.driver.find_element_by_class_name("ta-login-submit"))
        self.assertTrue(self.driver.find_element_by_class_name("ta-login-form"))

        #User sees the title of the page
        self.assertTrue("FRNKN" in self.driver.title)

        #User fills out form in order to login
        username = self.driver.find_element_by_id("id_username")
        password = self.driver.find_element_by_id("id_password")

        username.send_keys("cabedn")
        password.send_keys("HelloWorld12")

        self.driver.find_element_by_class_name("ta-login-submit").click()

        #The user gets redirected to /backlogs and sees the page title
        self.assertTrue("FRNKN" in self.driver.title)

        #The user sees a list with backlogs
        self.assertTrue(self.driver.find_element_by_class_name('ta-backlog-projects'))

        #He decides to use the first backlog and clicks on the button to navigate into the backlog detail view
        self.driver.find_element_by_class_name("NOT DEFINED") #Test implementation has to be finished



if __name__ == '__main__':
    unittest.main()
