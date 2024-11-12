from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

firefox_binary_path = r"C:\Program Files\Mozilla Firefox\Firefox.exe"

options = Options()
options.binary_location = firefox_binary_path

service = Service('C:/geckodriver/geckodriver.exe')

driver = webdriver.Firefox(service=service, options=options)
driver.get('https://reqres.in/api-docs/#/')

wait = WebDriverWait(driver, 5)

method_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='opblock-summary-method']")))
method_texts = [method.text for method in method_elements]

path_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='opblock-summary-path']")))
path_texts = [path.text for path in path_elements]

driver.quit()

post_body = {
  "email": "eve.holt@reqres.in",
  "password": "cityslicka"
}

base_url = "https://reqres.in/api"

