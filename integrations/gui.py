from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from integrations.interface import External
from schema import Data


class ExternalGui(External):
    driver = webdriver.Chrome()

    async def authenticate(self):
        self.driver.get(self.auth_url)

        field_user = self.driver.find_element(By.NAME, "username")
        field_pass = self.driver.find_element(By.NAME, "password")
        field_user.send_keys(self.username)
        field_pass.send_keys(self.password)

        field_pass.send_keys(Keys.RETURN)
        time.sleep(3)

    async def send_data(self, data: Data):
        field_name = self.driver.find_element(By.NAME, "name")
        field_birthday = self.driver.find_element(By.NAME, "birthday")
        field_document_number = self.driver.find_element(By.NAME, "document_number")
        field_document_type = self.driver.find_element(By.NAME, "document_type")

        field_name.send_keys(data.name)
        field_birthday.send_keys(data.birthday)
        field_document_number.send_keys(data.document_number)
        field_document_type.send_keys(data.document_type)

        button_submit = self.driver.find_element(By.NAME, "submit")
        button_submit.click()

        time.sleep(2)

    async def close(self):
        self.driver.quit()
