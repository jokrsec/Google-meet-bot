from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from config import *
from time import sleep


driver = webdriver.Firefox(executable_path="./geckodriver")
action = ActionChains(driver)


class GoogleLoginPage():
	email = "identifier"
	click_email = "identifierNext"
	password = "password"
	click_password = "passwordNext"

	def login(self):
		driver.get(GOOGLE_LOGIN_SERVICE)

		username = driver.find_element_by_name(self.email)
		username.clear()
		username.send_keys(GMAIL_IDENTIFIER)
		driver.find_element_by_id(self.click_email).click()

		sleep(2)

		password = driver.find_element_by_name(self.password)
		password.clear()
		password.send_keys(GMAIL_PASSWORD)
		driver.find_element_by_id(self.click_password).click()

class JoinMeet():
	join_button = 'div[role="button"]'
	leave_button = 'button[role="button"]'

	def join(self, location):
		driver.get(location)

		sleep(1)
		action.key_down(Keys.CONTROL).send_keys('d').key_up(Keys.CONTROL).perform()
		sleep(1)
		action.key_down(Keys.CONTROL).send_keys('e').key_up(Keys.CONTROL).perform()

		driver.find_elements_by_css_selector(self.join_button)[3].click()

		
	def leave(self):
		driver.find_elements_by_css_selector(self.leave_button)[5].click()
		print("\n[+]Left the class..")
		sleep(1)
		driver.close()


